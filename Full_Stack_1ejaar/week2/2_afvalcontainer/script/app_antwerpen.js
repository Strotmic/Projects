'use strict';

const handleData = function (
  url,
  callbackFunctionName,
  callbackErrorFunctionName = null,
  method = 'GET',
  body = null
) {
  fetch(url, {
    method: method,
    body: body,
    // headers: {
    //   'content-type': 'application/json'
    // },
  })
    .then(function (response) {
      if (!response.ok) {
        console.warn(
          `>> Probleem bij de fetch(). Statuscode: ${response.status}`
        );
        if (callbackErrorFunctionName) {
          console.warn(
            `>> Callback errorfunctie ${callbackErrorFunctionName.name}(response) wordt opgeroepen`
          );
          callbackErrorFunctionName(response);
        } else {
          console.warn(
            '>> Er is geen callback errorfunctie meegegeven als parameter'
          );
        }
      } else {
        console.info('>> Er is een response teruggekomen van de server');
        return response.json();
      }
    })
    .then(function (jsonObject) {
      if (jsonObject) {
        console.info('>> JSONobject is aangemaakt');
        console.info(
          `>> Callbackfunctie ${callbackFunctionName.name}(response) wordt opgeroepen`
        );
        callbackFunctionName(jsonObject);
      }
    })
    .catch(function (error) {
      console.warn(`>>fout bij verwerken json: error`);
      if (callbackErrorFunctionName) {
        callbackErrorFunctionName(undefined);
      }
    });
};

const zeroToStreep = function(getal){
  if(getal==0){
    return '---'
  }else{
    return getal
  }
}

const showDataAfvalContainers = function (jsonObject) {
  try{
      console.info(jsonObject);

  const straat = jsonObject.features;
  let htmlString = '';

  for (let i of straat) {
    htmlString += `<article class="c-locatie">
      <h2 class="c-locatie__adres">${zeroToStreep(i.properties.STRAATNAAM)}</h2>
      <div class="c-locatie__info">
        <div class="c-locatie__type">GFT
          <div class="c-locatie__aantal">${zeroToStreep(
            i.properties.AANTAL_CNTR_GFT
          )}</div>
        </div>
        <div class="c-locatie__type">GLAS
          <div class="c-locatie__aantal">${zeroToStreep(
            i.properties.AANTAL_CNTR_GLAS
          )}</div>
        </div>
        <div class="c-locatie__type">PMD
          <div class="c-locatie__aantal">${zeroToStreep(
            i.properties.AANTAL_CNTR_PMD
          )}</div>
        </div>
        <div class="c-locatie__type">REST
          <div class="c-locatie__aantal">${zeroToStreep(
            i.properties.AANTAL_CNTR_REST
          )}</div>
        </div>
        <div class="c-locatie__type">PAPIER
          <div class="c-locatie__aantal">${
            zeroToStreep(i.properties.AANTAL_CNTR_PK
          )}</div>
        </div>
      </div>
    </article>`;
  }

  const htmlPlace = document.querySelector('.js-placeholder');
  htmlPlace.innerHTML = htmlString;
  } catch(err){
    console.error('Er ging iets mis')

  }

};

const getDataAfvalContainers = function (url) {
  handleData(url, showDataAfvalContainers);
};

const init = function () {
  console.info('loaded');

  // const url = 'https://opendata.arcgis.com/datasets/413c00cfda8743fbb94ce7e7e67d67c7_49.geojson';
  const url = 'https://www.diero.be/MCT/JSON/vuilnis.json';
  getDataAfvalContainers(url);
};

document.addEventListener('DOMContentLoaded', init);
