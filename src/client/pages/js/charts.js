//
sentiment_labels      = ['4/7/18', '4/8/18', '4/9/18', '4/10/18', '4/11/18', '4/12/18', '4/13/18', '4/14/18', '4/15/18', '4/16/18', '4/17/18', '4/18/18', '4/19/18', '4/20/18', '4/21/18', '4/22/18', '4/23/18', '4/24/18', '4/25/18', '4/26/18', '4/27/18', '4/28/18', '4/29/18', '4/30/18', '5/1/18', '5/2/18', '5/3/18', '5/4/18', '5/5/18', '5/6/18'];
sentiment_sentiments  = [0.481, 0.501, 0.522, 0.479, 0.47, 0.551, 0.529, 0.579, 0.569, 0.562, 0.537, 0.542, 0.577, 0.626, 0.587, 0.582, 0.591, 0.584, 0.599, 0.597, 0.589, 0.56, 0.61, 0.604, 0.578, 0.609, 0.586, 0.58, 0.584, 0.549];
sentiment_btc_prices  = [6927.69, 7017.66, 6699.27, 6787.57, 6926.27, 7847.85, 7895.41, 8036.51, 8340.75, 8043.8, 7895.42, 8164.94, 8254.63, 8852.72, 8807.21, 8838.55, 8933.86, 9555.54, 8995.51, 9258.4, 9010.32, 9326.17, 9334.28, 9259.57, 9075.14, 9221.43, 9639.27, 9710.73, 9803.31, 9630.14];

// SENTIMENT CHART
var canvas = document.getElementById('sentiment-chart');
new Chart(canvas, {
  type: 'line',
  data: {
    labels: sentiment_labels,
    datasets: [{
      	label:'BTC/USD CLOSING PRICE',
      	yAxisID: 'A',
      	data: sentiment_btc_prices,
      	backgroundColor: ['rgba(255, 99, 132, 0.2)'],
      	borderColor: ['rgba(255,99,132,1)'],
        borderWidth: 1
    }, {
    	label: 'SENTIMENT ANALYSIS',
      	yAxisID: 'B',
      	data: sentiment_sentiments,
      	backgroundColor: ['rgba(46, 207, 255, 0.2)'],
        borderColor: ['rgba(46,207,255,1)'],
        borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        id: 'A',
        type: 'linear',
        position: 'left',
      }, {
        id: 'B',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 1,
          min: 0
        }
      }]
    }
  }
});


// OTHER STRATEGIES CHART
other_strat_labels = ['4/24/2018', '4/25/2018', '4/26/2018', '4/27/2018', '4/28/2018', '4/29/2018', '4/30/2018', '5/1/2018', '5/2/2018', '5/3/2018', '5/4/2018', '5/5/2018', '5/6/2018', '5/7/2018', '5/8/2018', '5/9/2018', '5/10/2018', '5/11/2018', '5/12/2018', '5/13/2018', '5/14/2018', '5/15/2018', '5/16/2018', '5/17/2018', '5/18/2018', '5/19/2018', '5/20/2018', '5/21/2018', '5/22/2018'];
other_strat_returns = [1.011, 1.081, 1.018, 1.048, 1.019, 1.055, 1.056, 1.048, 1.027, 1.043, 1.091, 1.099, 1.109, 1.09, 1.057, 1.044, 1.055, 1.03, 0.958, 0.96, 0.987, 0.979, 0.963, 0.944, 0.917, 0.932, 0.93, 0.963, 0.949];
other_strat_5   = [1.011, 1.081, 1.018, 1.048, 1.019, 1.055, 1.056, 1.065, 1.043, 1.027, 1.073, 1.081, 1.092, 1.072, 1.041, 1.028, 1.017, 1.042, 1.12, 1.118, 1.087, 1.096, 1.114, 1.137, 1.17, 1.151, 1.153, 1.115, 1.131];
other_strat_10 = [1.011, 1.081, 1.018, 1.048, 1.019, 1.055, 1.056, 1.048, 1.027, 1.043, 1.091, 1.099, 1.109, 1.09, 1.057, 1.044, 1.034, 1.059, 1.138, 1.136, 1.104, 1.114, 1.132, 1.155, 1.189, 1.169, 1.172, 1.133, 1.149];
other_strat_15 = [1.011, 1.081, 1.018, 1.048, 1.019, 1.055, 1.056, 1.048, 1.027, 1.043, 1.091, 1.099, 1.109, 1.09, 1.057, 1.044, 1.055, 1.08, 1.005, 1.003, 0.975, 0.984, 1.0, 1.021, 1.05, 1.033, 1.035, 1.001, 1.015];
other_strat_20 = [1.011, 1.081, 1.018, 1.048, 1.019, 1.055, 1.056, 1.048, 1.027, 1.043, 1.091, 1.099, 1.109, 1.09, 1.057, 1.044, 1.055, 1.03, 0.958, 0.956, 0.93, 0.938, 0.953, 0.973, 1.001, 0.985, 0.987, 0.954, 0.968];

var canvas = document.getElementById('other-strategy-chart');
new Chart(canvas, {
  type: 'line',
  data: {
    labels: other_strat_labels,
    datasets: [
    {
        label:'RETURNS',
        yAxisID: 'A',
        data: other_strat_returns,
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
        borderColor: ['rgba(0,0,0,1)'],
        borderWidth: 1
    }, {
      label: 'WINDOW SIZE 5',
        yAxisID: 'B',
        data: other_strat_5,
        backgroundColor: ['rgba(204, 255, 204, 0.2)'],
        borderColor: ['rgba(204, 255, 204,1)'],
        borderWidth: 1
    }, {
      label: 'WINDOW SIZE 10',
        yAxisID: 'B',
        data: other_strat_10,
        backgroundColor: ['rgba(128, 0, 0, 0.2)'],
        borderColor: ['rgba(128, 0, 0,1)'],
        borderWidth: 1
    },{
      label: 'WINDOW SIZE 15',
        yAxisID: 'B',
        data: other_strat_15,
        backgroundColor: ['rgba(153, 102, 255, 0.2)'],
        borderColor: ['rgba(153, 102, 255,1)'],
        borderWidth: 1
    }, {
      label: 'WINDOW SIZE 20',
        yAxisID: 'B',
        data: other_strat_20,
        backgroundColor: ['rgba(255, 255, 0, 0.2)'],
        borderColor: ['rgba(255, 255, 0,1)'],
        borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        id: 'A',
        type: 'linear',
        position: 'left',
        ticks: {
          max: 1.5,
          min: 0.5
        }
      }, {
        id: 'B',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 1.5,
          min: 0.5
        }
      }]
    }
  }
});


// POLYNOMIAL REGRESSION CHART
poly_labels = ['04/22/2018', '04/23/2018', '04/24/2018', '04/25/2018', '04/26/2018', '04/27/2018', '04/28/2018', '05/01/2018', '05/02/2018', '05/03/2018', '05/04/2018', '05/05/2018', '05/06/2018', '05/07/2018', '05/08/2018', '05/09/2018', '05/10/2018', '05/11/2018', '05/12/2018', '05/13/2018', '05/14/2018', '05/15/2018', '05/16/2018', '05/17/2018', '05/18/2018', '05/19/2018', '05/20/2018', '05/21/2018', '05/22/2018', '05/23/2018'];
poly_actual_price = [8933.862, 9555.542, 8995.507, 9258.398, 9010.32, 9326.173, 9334.282, 9259.57, 9075.137, 9221.426, 9639.268, 9710.73, 9803.307, 9630.136, 9345.69, 9228.608, 9322.042, 9101.483, 8468.788, 8484.347, 8727.652, 8652.038, 8511.458, 8340.703, 8106.118, 8240.055, 8223.288, 8507.407, 8385.556, 8015.58];
poly_predicted_price = [9248.239, 11106.345, 11652.144, 10757.371, 11645.69, 10224.869, 9162.207, 9792.134, 9274.22, 10835.159, 10402.329, 12172.284, 9741.152, 9331.011, 10568.638, 11482.476, 9297.641, 9243.931, 12327.539, 9437.448, 9238.531, 11018.65, 10209.034, 9402.904, 10162.175, 10780.395, 9394.367, 9234.424, 10150.277, 9835.315];

var canvas = document.getElementById('poly-chart');
new Chart(canvas, {
  type: 'line',
  data: {
    labels: poly_labels,
    datasets: [{
        label:'BTC/USD CLOSING PRICE',
        yAxisID: 'A',
        data: poly_actual_price,
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
        borderColor: ['rgba(255,99,132,1)'],
        borderWidth: 1
    }, {
      label: 'POLYNOMIAL REGRESSION PREDICTED PRICE',
        yAxisID: 'B',
        data: poly_predicted_price,
        backgroundColor: ['rgba(46, 207, 255, 0.2)'],
        borderColor: ['rgba(46,207,255,1)'],
        borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        id: 'A',
        type: 'linear',
        position: 'left',
        ticks: {
          max: 15000,
          min: 5000
        }
      }, {
        id: 'B',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 15000,
          min: 5000
        }
      }]
    }
  }
});

// LSTM CHART
lstm_labels = ['05/02/2018', '05/03/2018', '05/04/2018', '05/05/2018', '05/06/2018', '05/07/2018', '05/08/2018', '05/09/2018', '05/10/2018', '05/11/2018', '05/12/2018', '05/13/2018', '05/14/2018', '05/15/2018', '05/16/2018', '05/17/2018', '05/18/2018', '05/19/2018', '05/20/2018', '05/21/2018', '05/22/2018'];
lstm_actual_price = [8933.862, 9555.542, 8995.507, 9258.398, 9010.32, 9326.173, 9334.282, 9259.57, 9075.137, 9221.426, 9639.268, 9710.73, 9803.307, 9630.136, 9345.69, 9228.608, 9322.042, 9101.483, 8468.788, 8484.347, 8727.652];
lstm_predicted_price = [8728.889, 8541.431, 8830.509, 9136.123, 8809.166, 8823.129, 8813.0, 8877.081, 8833.229, 8921.672, 8798.678, 8872.329, 9020.683, 9039.711, 9051.532, 8782.877, 9015.651, 8997.987, 8896.112, 8866.573, 9012.359];

var canvas = document.getElementById('lstm-chart');
new Chart(canvas, {
  type: 'line',
  data: {
    labels: lstm_labels,
    datasets: [{
        label:'BTC/USD CLOSING PRICE',
        yAxisID: 'A',
        data: lstm_actual_price,
        backgroundColor: ['rgba(255, 99, 132, 0.2)'],
        borderColor: ['rgba(255,99,132,1)'],
        borderWidth: 1
    }, {
      label: 'LSTM PREDICTED PRICE',
        yAxisID: 'B',
        data: lstm_predicted_price,
        backgroundColor: ['rgba(46, 207, 255, 0.2)'],
        borderColor: ['rgba(46,207,255,1)'],
        borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        id: 'A',
        type: 'linear',
        position: 'left',
        ticks: {
          max: 10000,
          min: 5000
        }
      }, {
        id: 'B',
        type: 'linear',
        position: 'right',
        ticks: {
          max: 10000,
          min: 5000
        }
      }]
    }
  }
});
