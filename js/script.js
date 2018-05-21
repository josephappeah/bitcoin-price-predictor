server 			= "http://localhost:3000";
displayTweets 	= [];
sentiment_text 		= "NEUTRAL";
sentiment_color  	= "#FFC107";
price_text 			= "$---";
price_color  		= "#FFC107";
prediction_text 	= "RISE";
prediction_color  	= "#FFC107";

function getTodaySentimentInformation() {
	axios.get(server + "/get-todays-sentiments")
	  .then(function (response) {
	    console.log(response.data);
	    updateChancesText(response.data.rating);
	    updateTweetsOnHomepage(response.data.sentiments);
	})
	  .catch(function (error) {
	    console.log(error);
	});
}

/*
sentiment_labels = ['11/22/17', '11/23/17', '11/24/17', '11/25/17', '11/26/17', '11/27/17', '11/28/17', '11/29/17', '11/30/17', '12/1/17', '12/2/17', '12/3/17', '12/4/17', '12/5/17', '12/6/17', '12/7/17', '12/8/17', '12/9/17', '12/10/17', '12/11/17', '12/12/17', '12/13/17', '12/14/17', '12/15/17', '12/16/17', '12/17/17', '12/18/17', '12/19/17', '12/20/17', '12/21/17', '12/22/17', '12/23/17', '12/24/17', '12/25/17', '12/26/17', '12/27/17', '12/28/17', '12/29/17', '12/30/17', '12/31/17', '1/1/18', '1/2/18', '1/3/18', '1/4/18', '1/5/18', '1/6/18', '1/7/18', '1/8/18', '1/9/18', '1/10/18', '1/11/18', '1/12/18', '1/13/18', '1/14/18', '1/15/18', '1/16/18', '1/17/18', '1/18/18', '1/19/18', '1/20/18', '1/21/18', '1/22/18', '1/23/18', '1/24/18', '1/25/18', '1/26/18', '1/27/18', '1/28/18', '1/29/18', '1/30/18', '1/31/18', '2/1/18', '2/2/18', '2/3/18', '2/4/18', '2/5/18', '2/6/18', '2/7/18', '2/8/18', '2/9/18', '2/10/18', '2/11/18', '2/12/18', '2/13/18', '2/14/18', '2/15/18', '2/16/18', '2/17/18', '2/18/18', '2/19/18', '2/20/18', '2/21/18', '2/22/18', '2/23/18', '2/24/18', '2/25/18', '2/26/18', '2/27/18', '2/28/18', '3/1/18', '3/2/18', '3/3/18', '3/4/18', '3/5/18', '3/6/18', '3/7/18', '3/8/18', '3/9/18', '3/10/18', '3/11/18', '3/12/18', '3/13/18', '3/14/18', '3/15/18', '3/16/18', '3/17/18', '3/18/18', '3/19/18', '3/20/18', '3/21/18', '3/22/18', '3/23/18', '3/24/18', '3/25/18', '3/26/18', '3/27/18', '3/28/18', '3/29/18', '3/30/18', '3/31/18', '4/1/18', '4/2/18', '4/3/18', '4/4/18', '4/5/18', '4/6/18', '4/7/18', '4/8/18', '4/9/18', '4/10/18', '4/11/18', '4/12/18', '4/13/18', '4/14/18', '4/15/18', '4/16/18', '4/17/18', '4/18/18', '4/19/18', '4/20/18', '4/21/18', '4/22/18', '4/23/18', '4/24/18', '4/25/18', '4/26/18', '4/27/18', '4/28/18', '4/29/18', '4/30/18', '5/1/18', '5/2/18', '5/3/18', '5/4/18', '5/5/18', '5/6/18'];
sentiment_sentiments = [0.59, 0.591, 0.572, 0.561, 0.598, 0.594, 0.642, 0.638, 0.64, 0.798, 0.804, 0.83, 0.858, 0.842, 0.897, 0.888, 0.899, 0.848, 0.891, 0.864, 0.865, 0.854, 0.898, 0.907, 0.914, 0.918, 0.911, 0.914, 0.88, 0.825, 0.762, 0.777, 0.734, 0.702, 0.751, 0.763, 0.703, 0.713, 0.609, 0.607, 0.567, 0.651, 0.682, 0.673, 0.721, 0.866, 0.869, 0.765, 0.729, 0.61, 0.591, 0.612, 0.739, 0.573, 0.594, 0.561, 0.557, 0.541, 0.546, 0.567, 0.514, 0.524, 0.528, 0.565, 0.535, 0.495, 0.558, 0.549, 0.537, 0.481, 0.54, 0.526, 0.468, 0.48, 0.477, 0.437, 0.52, 0.327, 0.38, 0.366, 0.443, 0.433, 0.517, 0.53, 0.53, 0.593, 0.609, 0.577, 0.586, 0.582, 0.597, 0.602, 0.512, 0.516, 0.545, 0.54, 0.58, 0.589, 0.576, 0.571, 0.605, 0.585, 0.599, 0.597, 0.611, 0.578, 0.576, 0.526, 0.513, 0.619, 0.533, 0.551, 0.517, 0.53, 0.533, 0.458, 0.561, 0.547, 0.59, 0.572, 0.611, 0.637, 0.571, 0.513, 0.601, 0.513, 0.499, 0.514, 0.475, 0.521, 0.482, 0.497, 0.529, 0.522, 0.504, 0.487, 0.481, 0.501, 0.522, 0.479, 0.47, 0.551, 0.529, 0.579, 0.569, 0.562, 0.537, 0.542, 0.577, 0.626, 0.587, 0.582, 0.591, 0.584, 0.599, 0.597, 0.589, 0.56, 0.61, 0.604, 0.578, 0.609, 0.586, 0.58, 0.584, 0.549];
sentiment_btc_prices =  [8230.69, 8002.64, 8201.46, 8763.78, 9326.59, 9739.05, 9908.23, 9816.35, 9916.54, 10859.56, 10895.01, 11180.89, 11616.85, 11696.06, 13708.99, 16858.02, 16057.14, 14913.4, 15036.96, 16699.68, 17178.1, 16407.2, 16531.08, 17601.94, 19343.04, 19086.64, 18960.52, 17608.35, 16454.72, 15561.05, 13857.14, 14548.71, 13975.44, 13917.03, 15745.26, 15378.28, 14428.76, 14427.87, 12629.81, 13860.14, 13412.44, 14740.76, 15134.65, 15155.23, 16937.17, 17135.84, 16178.49, 14970.36, 14439.47, 14890.72, 13287.26, 13812.71, 14188.78, 13619.03, 13585.9, 11348.02, 11141.25, 11250.65, 11514.92, 12759.64, 11522.86, 10772.15, 10839.83, 11399.52, 11137.24, 11090.06, 11407.15, 11694.47, 11158.39, 10035.0, 10166.51, 9052.58, 8827.63, 9224.39, 8186.65, 6914.26, 7700.39, 7581.8, 8237.24, 8689.84, 8556.61, 8070.8, 8891.21, 8516.24, 9477.84, 10016.49, 10178.71, 11092.15, 10396.63, 11159.72, 11228.24, 10456.17, 9830.43, 10149.46, 9682.38, 9586.46, 10313.08, 10564.42, 10309.64, 10907.59, 11019.52, 11438.65, 11477.41, 11595.54, 10763.2, 10118.06, 9429.11, 9089.28, 8746.0, 9761.4, 9182.84, 9154.7, 8151.53, 8358.12, 8530.4, 7993.67, 8171.42, 8412.03, 8986.95, 8947.75, 8690.41, 8686.83, 8662.38, 8617.3, 8197.55, 7876.2, 7960.38, 7172.28, 6882.53, 6935.48, 6794.11, 7035.85, 7410.44, 6787.76, 6826.51, 6603.88, 6927.69, 7017.66, 6699.27, 6787.57, 6926.27, 7847.85, 7895.41, 8036.51, 8340.75, 8043.8, 7895.42, 8164.94, 8254.63, 8852.72, 8807.21, 8838.55, 8933.86, 9555.54, 8995.51, 9258.4, 9010.32, 9326.17, 9334.28, 9259.57, 9075.14, 9221.43, 9639.27, 9710.73, 9803.31, 9630.14];


var canvas = document.getElementById('myChart');
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
*/

//
function setBitcoinStatus(){
	//document.getElementsByClassName("our-btc-sentiment").innerHTML 	= sentiment_text;
	$(".our-btc-sentiment").text(sentiment_text);
	$(".our-btc-sentiment").css("color", sentiment_color);

	$(".our-btc-price").text(price_text);
	$(".our-btc-price").css("color", price_color);

	$(".our-btc-prediction").text(prediction_text);
	$(".our-btc-prediction").css("color", prediction_color);
}


//
function updatePredictions(price, sentiment, prediction) {

	//
	if (sentiment > 0.6) {
		sentiment_text 	= "POSITIVE";
		sentiment_color = "#00C853";
	} else if (sentiment < 0.3) {
		sentiment_text 	= "NEGATIVE";
		sentiment_color = "#E53935";
	} 
	//


	//

	//
	if (price != null) {
		price_text 		= price;
		price_color 	= "#00C853";
	} 

	//else if (sentiment < 0.3) {
	//	sentiment_text 	= "LOW";
	//	sentiment_color = "#E53935";
	//} 
	//



	

	//
	if (prediction == true) {
		prediction_text 	= "RISE";
		prediction_color = "#00C853";
	} else if (prediction == false) {
		prediction_text 	= "FALL";
		prediction_color = "#E53935";
	} 
	//
}

function updateChancesText(rating) {

	//
	chance = "MEDIUM";
	color  = "#FFC107";

	//
	if (rating > 0.7) {
		chance = "HIGH";
		color  = "#00C853";
	} else if (rating < 0.3) {
		chance = "LOW";
		color = "#E53935";
	} 

	//
	document.getElementById("chance-text").innerHTML = chance;
	$("#chance-text").css("color", color);
	$(".chance-text").removeClass("blink");
}

//
function scrollToDiv(button_id, div_id){
	$(document).ready(function(){
		$("#"+ button_id).click(function(){
			$('html,body').animate({
				scrollTop: $("#" + div_id).offset().top - 90
			});
		});
	});
}


//
function updateTweetsOnHomepage(tweets) {
	//
	tweet_cards = '';

	//
	for (i = 0; i < tweets.length; i++) {
		tweet_cards += createTweetCards(tweets[i]);
	}

	//
	document.getElementById('sample-tweet-cards').innerHTML = tweet_cards;
	$("#loading-icon").removeClass('blink');

}


//
function createTweetCards(tweet) {
	//
	return '<div class="animated slideInDown" id="tweet-display-card" class="col-sm-12">' +
	        	'<div id="tweet-display-card-tweet" class="col-sm-9">' + 
	        		'<p><i>"' + tweet[0] + '"</i></p>' + 
	        	'</div>' + 
	        	'<div id="tweet-display-card-rating" class="col-sm-3">' +
	        		'<p>' + tweet[1] + '</p>' +
	        	'</div>' +
	        '</div>';
}

function blink_text() {
    $('.blink').fadeOut(750);
    $('.blink').fadeIn(750);
}

//
$('#popoverData').popover();
$('#popoverOption').popover({ trigger: "hover" });


//
function pushToHome(){
	return new Promise (function(resolve, reject) {
		window.location.href="home.html";
		resolve(true);
	})
	
}

//
function getBitcoinStatus() {
	axios.get(server + "/get-btc-status")
	  .then(function (response) {
	    pushToHome()
	    .then(function(){
	    	updatePredictions(response.data.price, response.data.sentiment, response.data.prediction);
	    })
	})
	  .catch(function (error) {
	    console.log(error);
	});
}

//
function startUp(){
	getBitcoinStatus();
}



//
//getTodaySentimentInformation();
scrollToDiv('find-out-why', 'lstm-heading');
scrollToDiv('about', 'lstm-heading');
setInterval(blink_text, 1000);