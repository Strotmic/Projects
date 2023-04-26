'use strict';
let currentDestinationID; //is geen DOM/HTML reference maar globale variabele
let bestemmingObject;
//#region ***  DOM references                           ***********
let htmlDestination,
  htmlRoute,
  htmlSelectedCity,
  htmlDestinationSelect,
  htmlAdaptTrain,
  map,
  layergroup;

let NMBSIcon = L.icon({
  iconUrl: './assets/marker.svg',
  shadowUrl: './assets/markershadow.svg',

  iconSize: [38, 95], // size of the icon
  shadowSize: [50, 64], // size of the shadow
  iconAnchor: [22, 94], // point of the icon which will correspond to marker's location
  shadowAnchor: [4, 62], // the same for the shadow
  popupAnchor: [-3, -76], // point from which the popup should open relative to the iconAnchor
});

//#endregion
const provider = 'https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png';
const copyright =
  '&copy; <a href="https://www.openstreetmap.org/copyright%22%3EOpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>';

//#region ***  Callback-Visualisation - show___         ***********

const showBestemming = function (jsonObject) {
  const data = jsonObject['data'];
  sessionStorage.setItem('test', JSON.stringify(jsonObject));
  console.log(sessionStorage.getItem(bestemmingObject));
  let htmlString = '';
  let htmlStringOption = '';
  try {
    for (let i of data) {
      htmlString += `<li class="c-sidebar-item"><button class="c-sidebar-button js-station" data-destination-id="${i['idbestemming']}">${i['stad']}</button></li>`;

      htmlStringOption += `<option value="${i['idbestemming']}">${i['stad']}</option>`;
    }
    htmlDestination.innerHTML = htmlString;
    htmlDestinationSelect.innerHTML = htmlStringOption;
    listenToNav();
  } catch (err) {
    console.error(err);
  }
};

const showTitle = function (x) {
  let htmlString = '';
  htmlString += x;
  htmlSelectedCity.innerHTML = htmlString;
};

const showTrainsOnDestinations = function (x) {
  const data = x['data'];
  if (x.length == 0) {
    htmlRoute.innerHTML = 'No trains';
  } else {
    let htmlString = '';
    for (let i of data) {
      let vertraging = '-';
      let afgeschaft = 'cancelled';
      let afgeschaftCl = 'c-traject__cancelled-label';
      if (i['vertraging'] != null) {
        vertraging = i['vertraging'];
      }
      if (i['afgeschaft'] == 0) {
        afgeschaft = '';
        afgeschaftCl = 'c-traject__cancelled';
      }

      htmlString += `
      <div class="c-traject">
          <div class="c-traject__info">
            <h2 class="c-traject__name">${i['stad']}</h2>
            <p class="c-traject__train-id">${i['idtrein']}</p>
          </div>
          <div class="c-traject__departure">${i['vertrek']}</div>
          <div class="c-traject__track">${i['spoor']}</div>
          <div class="c-traject__delay">${vertraging}</div>
          <div class="c-traject__cancelled">
            <span class="${afgeschaftCl}">${afgeschaft}</span>
          </div>
          <div class="c-traject__updatevertraging">
            <a href="vertraging.html?TreinID=${i['idtrein']}">
              <svg class="c-traject__updatevertraging-symbol" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round">
                <polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>
              </svg>
            </a>
          </div>
          <div class="c-traject__update">
            <a href="aanpassen.html?TreinID=${i['idtrein']}">
              <svg class="c-traject__update-symbol" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round">
                <polygon points="16 3 21 8 8 21 3 21 3 16 16 3"></polygon>
              </svg>
            </a>
          </div>
          <div class="c-traject__delete">
            <svg class="c-traject__delete-symbol" data-train-id="${i['idtrein']}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#222222" stroke-width="2" stroke-linecap="round">
              <polyline points="3 6 5 6 21 6"></polyline>
              <path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path>
              <line x1="10" y1="11" x2="10" y2="17"></line>
              <line x1="14" y1="11" x2="14" y2="17"></line>
            </svg>
          </div>
        </div>`;
    }
    htmlRoute.innerHTML = htmlString;
  }
  listenToClickRemoveTrain();
  listenToClickAddTrain();
};

const showUpdateTrain = function (x) {
  let htmlStringOption = '';
  console.info(x);
  let lijst = JSON.parse(sessionStorage.getItem('test'));
  console.info(lijst['data']);
  const js_adapttrain_idtrein = (document.querySelector(
    '.js-adapttrain-idtrein'
  ).value = x['treinen']['idtrein']);
  const js_adapttrain_vertrek = (document.querySelector(
    '.js-adapttrain-vertrek'
  ).value = x['treinen']['vertrek']);
  const js_adapttrain_spoor = (document.querySelector(
    '.js-adapttrain-spoor'
  ).value = x['treinen']['spoor']);
  const js_adapttrain_vertraging = (document.querySelector(
    '.js-adapttrain-vertraging'
  ).value = x['treinen']['vertraging']);
  const js_adapttrain_bestemmingid = document.querySelector(
    '.js-adapttrain-bestemmingid'
  );
  for (let i of lijst['data']) {
    htmlStringOption += `<option value="${i['idbestemming']}">${i['stad']}</option>`;
  }
  js_adapttrain_bestemmingid.innerHTML = htmlStringOption;
  js_adapttrain_bestemmingid.value = x['treinen']['bestemmingID'];
  listenToUpdateTrain();
};

const showError = function (error) {
  console.info(error);
};

const showDestinationsForMap = function (x) {
  console.info(x['data']);
  let htmlString = ' <ul class="c-add-locations">';
  for (let i of x['data']) {
    htmlString += `<li class="c-show-location js-location" data-lat="${i.latitude}" data-long="${i.Llngitude}">${i.stad}</li>`;
  }
  htmlString += '</ul>';
  document.querySelector('.js-locations').innerHTML = htmlString;
  listenToClickShowOnMap();
};
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***********
const callbackAddTrain = function (data) {
  console.log('ADD antw van server ');
  if (data.treinid > 0) {
    console.log('ADD gelukt');
  }
};

const callbackUpdateTrain = function () {
  console.log('geupdate');
  location.href = 'index.html';
};

const callbackRemoveTrain = function (data) {
  console.info('Trein verwijdert');
  getTreinenMetBestemming(currentDestinationID);
};
//#endregion

//#region ***  Data Access - get___                     ***********

const get_bestemmingen = function () {
  const url = 'http://127.0.0.1:5000/api/v1/bestemmingen/';
  handleData(url, showBestemming, showError);
};

const getTreinenMetBestemming = function (destination) {
  const url = `http://127.0.0.1:5000/api/v1/treinen/bestemming/${destination}/`;
  handleData(url, showTrainsOnDestinations);
};

const getTreinUpdate = function () {
  let urlParams = new URLSearchParams(window.location.search);
  let treinid = urlParams.get('TreinID');
  if (treinid != undefined) {
    handleData(
      `http://127.0.0.1:5000/api/v1/treinen/${treinid}/`,
      showUpdateTrain,
      showError
    );
  } else {
    console.error('fout verkeerd id');
  }
};

const getDestinationsForMap = function () {
  handleData(
    'http://127.0.0.1:5000/api/v1/bestemmingen/',
    showDestinationsForMap
  );
};

//#endregion

//#region ***  Event Listeners - listenTo___            ***********
const listenToClickShowOnMap = function () {
  for (let li of document.querySelectorAll('.js-location')) {
    li.addEventListener('click', function () {
      layergroup.clearLayers();
      L.marker(
        [this.getAttribute('data-lat'), this.getAttribute('data-long')],
        { icon: NMBSIcon }
      )
        .addTo(map)
        .bindPopup(this.innerHTML)
        .openPopup();
    });
  }
};

const listenToNav = function () {
  for (let i of document.querySelectorAll('.js-station')) {
    i.addEventListener('click', function () {
      currentDestinationID = this.getAttribute('data-destination-id');
      showTitle(this.innerHTML);
      getTreinenMetBestemming(currentDestinationID);
    });
  }
};

const listenToClickRemoveTrain = function () {
  const btn = document.querySelectorAll('.c-traject__delete-symbol');
  for (const i of btn) {
    i.addEventListener('click', function () {
      const id = this.getAttribute('data-train-id');
      const url = `http://127.0.0.1:5000/api/v1/treinen/${id}/`;
      handleData(url, callbackRemoveTrain, null, 'DELETE');
    });
  }
};

const listenToClickAddTrain = function () {
  const test = document.querySelector('.js-add-train');
  test.addEventListener('click', function () {
    let vertraging = null;
    let afgeschaft = 0;
    if (document.querySelector('.js-add-vertraging').value != '') {
      vertraging = document.querySelector('.js-add-vertraging').value;
    }
    if (document.querySelector('.js-add-afgeschaft').value == 'on') {
      afgeschaft = 1;
    }
    let u = {
      afgeschaft: afgeschaft,
      bestemmingID: document.querySelector('.js-add-bestemming').value,
      spoor: document.querySelector('.js-add-spoor').value,
      vertraging: vertraging,
      vertrek: document.querySelector('.js-add-vertrek').value,
    };
    const url = 'http://127.0.0.1:5000/api/v1/treinen/';
    handleData(url, callbackAddTrain, showError, 'POST', JSON.stringify(u));
  });
};

const listenToUpdateTrain = function () {
  document
    .querySelector('.js-adapttrain-btn')
    .addEventListener('click', function () {
      console.info('cliekced');
      const js_adapttrain_idtrein = document.querySelector(
        '.js-adapttrain-idtrein'
      ).value;
      const js_adapttrain_vertrek = document.querySelector(
        '.js-adapttrain-vertrek'
      ).value;
      const js_adapttrain_spoor = document.querySelector(
        '.js-adapttrain-spoor'
      ).value;
      const js_adapttrain_vertraging = document.querySelector(
        '.js-adapttrain-vertraging'
      ).value;
      const js_adapttrain_bestemmingid = document.querySelector(
        '.js-adapttrain-bestemmingid'
      ).value;
      const js_adapttrain_afgeschaft = document.querySelector(
        '.js-adapttrain-afgeschaft'
      ).value;
      const data = {
        vertrek: js_adapttrain_vertrek,
        spoor: js_adapttrain_spoor,
        vertraging: js_adapttrain_vertraging,
        bestemmingID: js_adapttrain_bestemmingid,
        afgeschaft: js_adapttrain_afgeschaft,
      };
      console.info(data);
      const url = `http://127.0.0.1:5000/api/v1/treinen/${js_adapttrain_idtrein}/`;
      handleData(
        url,
        callbackUpdateTrain,
        showError,
        'PUT',
        JSON.stringify(data)
      );
    });
};

//#endregion

//#region ***  Init / DOMContentLoaded                  ***********
const init = function () {
  console.log('🚂', 'https://www.youtube.com/watch?v=8oVTXSntnA0');

  // Get some DOM, we created empty earlier.
  htmlDestination = document.querySelector('.js-destinations');
  htmlRoute = document.querySelector('.js-trajects');
  htmlSelectedCity = document.querySelector('.js-departure');
  htmlDestinationSelect = document.querySelector('.js-add-bestemming');
  htmlAdaptTrain = document.querySelector('.js-adapttrain');
  let jsAanwezig = document.querySelector('.js-adapttrain');
  if (jsAanwezig != undefined) {
    getTreinUpdate();
  } else {
    console.error('fout');
    get_bestemmingen();
  }
  map = L.map('mapid').setView([51.041026, 3.398512], 10);
  layergroup = L.layerGroup().addTo(map);
  L.tileLayer(provider, { attribution: copyright }).addTo(map);
  getDestinationsForMap();
};

document.addEventListener('DOMContentLoaded', init);
//#endregion
