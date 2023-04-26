'use strict';

const toonScore = function () {
  console.info('test');
  const score = document.querySelector('.js-range').value;
  document.querySelector('.js-score').innerHTML = score;
};

const init = function () {
  document.querySelector('.js-range').addEventListener('input', toonScore);
};

document.addEventListener('DOMContentLoaded', init);
