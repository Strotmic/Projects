'use strict';

// const showValidity = function (htmlElement, tekst) {
//   htmlElement.setCustomValidity('');

//   if (!htmlElement.validity.valid) {
//     htmlElement.setCustomValidity(tekst);
//     htmlElement.classList.add('u-is-invalid');
//   } else {
//     htmlElement.classList.remove('u-is-invalid');
//   }
// };
const getSpellen = function (url) {
  handleData(url, showSpellen, errorSpellen);
};
const showSpellen = function (jsonObject) {
  try {
    console.info(jsonObject);
    let htmlString = '';

    for (const spel of jsonObject) {
      console.info(spel.name);
      htmlString += `<option value="${spel.thumbnail}">${spel.name}</option>`;
    }
    document.querySelector('.js-spel').innerHTML += htmlString;
  } catch (err) {
    console.error('er is een foutje');
  }
};
const errorSpellen = function () {};
const listenToChangeGame = function () {
  console.info(this.value);
  document.querySelector('.js-img').setAttribute('src', this.value);
};
const listenToValidation = function () {};

const addEventListeners = function () {
  document
    .querySelector('.js-spel')
    .addEventListener('change', listenToChangeGame);
  document.querySelector('.js-naam').addEventListener('input', function () {
    this.checkValidity();
    console.info('checking');
  });
  document.querySelector('.js-naam').addEventListener('invalid', function () {
    console.info('OHNEE');
    this.setCustomValidity('Meer dan 2 tekens');
  });

  // document.querySelector('.js-voornaam').addEventListener('input', function () {
  //   this.checkValidity();
  //   console.info('checking');
  // });
  // document
  //   .querySelector('.js-voornaam')
  //   .addEventListener('invalid', function () {
  //     console.info('OHNEE');
  //     this.setCustomValidity('Meer dan 2 tekens');
  //   });
};

const init = function () {
  console.info('DOM geladen');
  const url = 'https://www.diero.be/MCT/JSON/spellen.json';
  getSpellen(url);
  addEventListeners();
};

document.addEventListener('DOMContentLoaded', init);
