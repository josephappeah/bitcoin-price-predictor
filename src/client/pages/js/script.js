server 			= "http://ec2-13-59-97-185.us-east-2.compute.amazonaws.com:3000";
displayTweets 		= [];
sentiment_text 		= "NEUTRAL";
sentiment_color  	= "#FFC107";
price_text 		= "$---";
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
