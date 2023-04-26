'use strict';

let htmlSearchText, htmlSearchBtn;
let htmlSectionInfoSender, htmlSectionTrackAndTrace;
let htmlSenderName, htmlSenderCode;
let htmlStepDropOff, htmlStepWarehouse, htmlStepOutForDel, htmlStepDel;
let htmlStepDropOffDate,
  htmlStepWarehouseDate,
  htmlStepOutForDelDate,
  htmlStepDelDate;

const disable = function () {
  htmlStepDropOff.classList.remove('c-step--done');
  htmlStepDropOff.classList.remove('c-step--active');

  htmlStepWarehouse.classList.remove('c-step--done');
  htmlStepWarehouse.classList.remove('c-step--active');

  htmlStepOutForDel.classList.remove('c-step--done');
  htmlStepOutForDel.classList.remove('c-step--active');

  htmlStepDel.classList.remove('c-step--done');
  htmlStepDel.classList.remove('c-step--active');
};
const maakSectionZichtbaar = function (x) {
  if (x) {
    htmlSectionInfoSender.classList.remove('u-hide');
    htmlSectionTrackAndTrace.classList.remove('u-hide');
  } else {
    htmlSectionInfoSender.classList.add('u-hide');
    htmlSectionTrackAndTrace.classList.add('u-hide');
  }
};

const toonTrackTraceStappen = function (jsonObject) {
  disable();
  const afgifte = jsonObject.detail.afgifte;
  const sorteer = jsonObject.detail.sorteercentrum;
  const onderweg = jsonObject.detail.onderweg;
  const bezorgd = jsonObject.detail.bezorgd;

  if (afgifte) {
    htmlStepDropOff.classList.add('c-step--done');
    htmlStepDropOffDate.innerHTML = afgifte;
    if (!sorteer) {
      htmlStepDropOff.classList.add('c-step--active');
    }
  }
  if (sorteer) {
    htmlStepWarehouse.classList.add('c-step--done');
    htmlStepWarehouseDate.innerHTML = sorteer;
    if (!onderweg) {
      htmlStepWarehouse.classList.add('c-step--active');
    }
  }
  if (onderweg) {
    htmlStepOutForDel.classList.add('c-step--done');
    htmlStepOutForDelDate.innerHTML = onderweg;
    if (!bezorgd) {
      htmlStepOutForDel.classList.add('c-step--active');
    }
  }
  if (bezorgd) {
    htmlStepDel.classList.add('c-step--done');
    htmlStepDelDate.innerHTML = bezorgd;
    if (bezorgd) {
      htmlStepDel.classList.add('c-step--active');
    }
  }
};

const showTrackTraceInfo = function (jsonObject) {
  try {
    console.info(jsonObject);
    const naam = jsonObject.detail.naam;
    const postcode = jsonObject.detail.postcode;
    htmlSenderName.innerHTML = naam;
    htmlSenderCode.innerHTML = postcode;
    maakSectionZichtbaar(true);
    toonTrackTraceStappen(jsonObject);
  } catch (err) {
    console.error(err);
  }
};

const showError = function () {
  console.error('Error');
};

const getTrackTraceInfo = function () {
  const pakket = htmlSearchText.value;
  handleData(
    `http://127.0.0.1:5000/api/v1/trace/${pakket}/`,
    showTrackTraceInfo,
    showError
  );
};

const addEventListeners = function () {
  // event toevoegen aan de button
  htmlSearchBtn.addEventListener('click', getTrackTraceInfo);
};

document.addEventListener('DOMContentLoaded', function () {
  console.info('DOM geladen');
  // Tekstveld en button
  htmlSearchText = document.querySelector('.js-search-txt');
  htmlSearchBtn = document.querySelector('.js-search-btn');
  // Sections
  htmlSectionInfoSender = document.querySelector('.js-section-info-sender');
  htmlSectionTrackAndTrace = document.querySelector('.js-section-trace');
  // Naam en postcode
  htmlSenderName = document.querySelector('.js-sender-name');
  htmlSenderCode = document.querySelector('.js-sender-code');
  // Stappen
  htmlStepDropOff = document.querySelector('.js-step-drop-off');
  htmlStepWarehouse = document.querySelector('.js-step-warehouse');
  htmlStepOutForDel = document.querySelector('.js-step-out-for-delivery');
  htmlStepDel = document.querySelector('.js-step-delivered');
  // Datumvelden
  htmlStepDropOffDate = document.querySelector('.js-step-drop-off-datum');
  htmlStepWarehouseDate = document.querySelector('.js-step-warehouse-datum');
  htmlStepOutForDelDate = document.querySelector(
    '.js-step-out-for-delivery-datum'
  );
  htmlStepDelDate = document.querySelector('.js-step-delivered-datum');

  addEventListeners();
});
