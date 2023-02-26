'use strict';

const zodiac = [
  'boogschutter',
  'kreeft',
  'leeuw',
  'maagd',
  'ram',
  'schorpioen',
  'steenbok',
  'stier',
  'tweelingen',
  'vissen',
  'waterman',
  'weegschaal',
];

const init = function () {
  const joker = generateJoker(6, 2);
  console.info(joker);
  const htmlResult = document.querySelector('.js-result');
  htmlResult.innerHTML = showWinningNumbers(joker);
};

const generateJoker = function (x, y) {
  const arrJoker = [];
  for (let i = 0; i < x; i++) {
    arrJoker.push(createRandomNumber(0, 9));
  }
  for (let i = 0; i < y; i++) {
    arrJoker.push(zodiac[createRandomNumber(0, 11)]);
  }
  return arrJoker;
};

const showWinningNumbers = function (x) {
  let result = '';
  for (let i = 0; i < x.length; i++) {
    if (Number.isInteger(x[i])) {
      result += `<div class="c-joker__trekking">${x[i]}</div>`;
    } else {
      result += ` <img src="images/zodiac/${x[i]}.webp" class="c-joker__trekking c-joker__img" alt="">`;
    }
  }
  return result;
};

const createRandomNumber = function (min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

init();
