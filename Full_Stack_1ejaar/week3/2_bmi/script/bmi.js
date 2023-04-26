'use strict';

let htmlGewicht, htmlLengte, htmlMijnButton;

const addEventListeners = function () {
  htmlGewicht.addEventListener('input', checkValues);
  htmlLengte.addEventListener('input', checkValues);
  htmlMijnButton.addEventListener('click', function () {
    const bmi = getBMIResult(htmlGewicht.value, htmlLengte.value);
    console.info(bmi);
  });
};

const checkValues = function () {
  const l = htmlLengte.value;
  const g = htmlGewicht.value;

  if (l >= 150 && l <= 200 && g >= 35 && g <= 200) {
    htmlMijnButton.disabled = false;
  } else {
    htmlMijnButton.disabled = true;
  }
};

const getBMIResult = function (g, l) {
  return g / ((l / 100) * (l / 100));
};

const init = function () {
  console.info('DOM geladen');
  htmlGewicht = document.querySelector('.js-gewicht');
  htmlLengte = document.querySelector('.js-lengte');
  htmlMijnButton = document.querySelector('.js-btn');

  htmlMijnButton.disabled = true;

  addEventListeners();
};

document.addEventListener('DOMContentLoaded', init);
