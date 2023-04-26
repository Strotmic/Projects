'use strict';

//#region ***  DOM references                           ***********
let htmlKleuren, htmlUitvoer, htmlInsert;
//#endregion

//#region ***  Callback-Visualisation - show___         ***********
const showKleuren = function (data) {
  let kleurenHTML = '';
  for (const kleur of data.colors) {
    kleurenHTML += `<li 
                      class="js-kleurelement" 
                      data-code="${kleur.code.hex}" 
                      data-category="${kleur.category}"
                    >
                    ${kleur.color}
                    </li>`;
  }
  htmlKleuren.innerHTML = kleurenHTML;
  listenToClickKleur();
};
//#endregion

//#region ***  Callback-No Visualisation - callback___  ***********

//#endregion

//#region ***  Data Access - get___                     ***********
const getKleuren = function () {
  console.info('kleuren worden geladen van API');
  handleData('data/kleuren.json', showKleuren);
};
//#endregion

//#region ***  Event Listeners - listenTo___            ***********

const listenToClickKleur = function () {
  const buttons = document.querySelectorAll('.js-kleurelement');
  for (const b of buttons) {
    b.addEventListener('click', function () {
      const gekozenCode = this.getAttribute('data-code');
      const gekozenCategorie = this.dataset.category;
      console.info(`b = ${b.dataset.code} en this = ${this.dataset.code}`);

      htmlUitvoer.innerText = `De gekozen kleur heeft een Hex waarde van ${gekozenCode} en behoort tot category ${gekozenCategorie}`;
      document.querySelector('body').style.backgroundColor = gekozenCode;
    });
  }
};
//#endregion

//#region ***  Init / DOMContentLoaded                  ***********
const init = function () {
  console.info('DOM geladen');
  htmlKleuren = document.querySelector('.js-kleuren');
  htmlInsert = document.querySelector('.js-insert');
  htmlUitvoer = document.querySelector('.js-uitvoer');

  //We checken in welke pagina we zitten.
  if (htmlKleuren) {
    getKleuren();
  }
  if (htmlInsert) {
    alert('Dit is een pagina die niet bestaat.');
  }
};

document.addEventListener('DOMContentLoaded', init);
//#endregion
