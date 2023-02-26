'use strict';

const verwerkSerie = function (jsonObject) {
  console.info(jsonObject);
  console.info(`De naam van de serie is ${jsonObject.name}`);
  console.info(`De uitzenddag is ${jsonObject.schedule.days[0]}`);
  console.info('Genres:');
  const genres = jsonObject.genres;

  for (const i of genres) {
    console.info(`- ${i}`);
  };

  let lijst ='<ul>';
  console.log('Overzicht episodes');
  const episodes = jsonObject._embedded.episodes;

  for (const i of episodes) {
    lijst+= (`<li> S${i.season} E${i.number} - ${i.name} </li>`);
  };

  lijst+=('</ul>')
  const htmlEpisodes = document.querySelector('.js-episodes');
  htmlEpisodes.innerHTML = lijst;
};

const laadSerieInfo = function (url) {
  console.info(`Op te zoeken URL: ${url} `);

  fetch(url)
    .then(function (response) {
      if (response.ok) {
        return response.json();
      }
    })
    .then(function (jsonObject) {
      verwerkSerie(jsonObject);
    });
};

const init = function () {
  console.info('loaded');

  const url =
    'http://api.tvmaze.com/singlesearch/shows?q=Stranger+Things&embed=episodes';
  laadSerieInfo(url);
};

document.addEventListener('DOMContentLoaded', init);
