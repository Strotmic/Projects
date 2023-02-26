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

const showWeatherData = function (e) {
  try {
    console.info(e);
    const htmlStad = document.querySelector('.js-city-placeholder');
    const htmlWeer = document.querySelector('.js-weather-placeholder')
    let htmlString = '';

    for(let i = 0 ; i< e.list.length; i+=8){
      htmlString += `${e.list[i].dt}`
    }

    htmlStad.innerHTML = e.city.name
    htmlWeer.innerHTML = htmlString;
  } catch (err) {
    console.error('error weeerdata weergeven');
  }
};

const getWeatherData = function (url) {
  handleData(url, showWeatherData);
};

const init = function () {
  console.info('loaded');
  const url =
    'http://api.openweathermap.org/data/2.5/forecast?q=kortrijk,BE&appid=3118a6a73ebfa0cb4c5184c8c379cfe5&units=metric&lang=nl';

  getWeatherData(url);
};

document.addEventListener('DOMContentLoaded', init);
