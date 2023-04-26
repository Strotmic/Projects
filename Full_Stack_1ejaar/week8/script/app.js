'use strict';
//#region ***  Callback-Visualisation - show___         ***********
const showData = function (x) {
  console.info(x);

  let labels = [];
  let data = [];

  for (const i of x) {
    labels.push(i.unit);
    data.push(i.price);
  }
  console.info(data);
  drawChart(labels, data);
};

const drawChart = function (labels, data) {
  var options = {
    series: [
      {
        data: data,
        name: 'Iphone Pricing',
      },
    ],
    labels: labels,
    chart: {
      type: 'line',
      height: 350,
    },
    stroke: {
      curve: 'stepline',
    },
    dataLabels: {
      enabled: false,
    },
    title: {
      text: 'Stepline Chart',
      align: 'left',
    },
    noData: {
      text: 'Loading/...',
    },
  };

  let chart = new ApexCharts(document.querySelector('.js-chart'), options);
  chart.render();
};
//#endregion

//#region ***  Data Access - get___                     ***********
const getData = function () {
  handleData('https://www.diero.be/MCT/JSON/iphone.json', showData);
};

//#endregion

//#region ***  Init / DOMContentLoaded                  ***********
const init = function () {
  console.log('test');
};

document.addEventListener('DOMContentLoaded', function () {
  getData();
});
//#endregion
