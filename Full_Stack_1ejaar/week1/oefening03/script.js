'use strict';

const zetNutriPuntOmNaarLetter = function (nutriPunt) {
  const dic = {'A':[-15,-1], 'B':[0,2],'C':[3,10],'D':[11,18],'E':[19,40]};
  for (const [key, value] of Object.entries(dic)) {
    if(nutriPunt<=value[1] && nutriPunt>=value[0] ){
      return key;
    }
  }
  return '';
};

const getCssClassForNutriScore = function (nutriScore) {
  const dic = {'A':'c-nutriscores__score--highest', 'B':'c-nutriscores__score--high ','C':'c-nutriscores__score--middle ','D':'c-nutriscores__score--low ','E':'c-nutriscores__score--lowest'};
  let letter ='';
  for (const [key, value] of Object.entries(dic)) {
    if(key == nutriScore){
      console.log(value);
      return value;
    }
  }
  return '';
};

const showNutriScore = function () {
  //array with integers between -15 and 40
  const arrNutriPunten = [8, -14, 5, 3, 40, -15, 0, 10, 20, 30];
  const htmlNutriScore = document.querySelector('.js-scores');
  let scores =[];
  let inhoud ='';

  for(let i in arrNutriPunten){
    scores.push(zetNutriPuntOmNaarLetter(arrNutriPunten[i]));
  };

  for(let i in scores){
    
    inhoud+=`<div class="c-nutriscores__score ${getCssClassForNutriScore(scores[i])}"></div>`
  };

  htmlNutriScore.innerHTML = inhoud;
};
const init = function () {
  console.log('Pagina geladen');
  showNutriScore()
};

document.addEventListener('DOMContentLoaded', init);