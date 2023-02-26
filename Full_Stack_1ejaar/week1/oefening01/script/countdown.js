'use strict';
const createRandomNumber = function (min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};

const createCountDown = function () {
  // commentaar
  let counter = '';
  let getal = 10;
  for (let i = getal; i > 0; i--) {
    counter += `<span class="c-number c-number--${i} ${getCSSClass(
      i
    )}">${i} ${setSpaces(2)}</span>`;
  }
  return counter;
};
const init = function () {
  const htmlHolder = document.querySelector('.js-holder');
  htmlHolder.innerHTML = createCountDown();
};

const getCSSClass = function (x) {
  if (x % 2 == 0) {
    return 'c-number--even';
  }

  return '';
};

const setSpaces= function(x){
    return '&nbsp'.repeat(x)
}

init();
