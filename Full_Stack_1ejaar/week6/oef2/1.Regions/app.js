'use strict';

// #region ***  DOM references                           ***********
// #endregion

// #region ***  Callback-Visualisation - show___         ***********
const showKlanten = function (jsonObject) {
  console.info(jsonObject);
};

const showBestemmigen = function (jsonObject) {
  console.info(jsonObject);
};
// #endregion

// #region ***  Callback-No Visualisation - callback___  ***********
const callbackError = function (err) {
  console.error(err);
};
// #endregion

// #region ***  Data Access - get___                     ***********
const getKlanten = function () {
  handledata('http://server/klanten', showKlanten, callbackError);
};
const getBestemmingen = function () {
  handledata('http://server/bestemmingen', showBestemmigen, callbackError);
};
// #endregion

// #region ***  Event Listeners - listenTo___            ***********
// #endregion

// #region ***  Init / DOMContentLoaded                  ***********
const init = function () {
  getKlanten();
  getBestemmingen();
};

document.addEventListener('DOMContentLoaded', init);
// #endregion


mct