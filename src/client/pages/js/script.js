//===========================================================================================
server 			= "http://ec2-13-59-97-185.us-east-2.compute.amazonaws.com:3000";
//server 				= "http://localhost:3000";
displayTweets 		= [];

//===========================================================================================



//utils =====================================================================================


// update the predictions on the header with data from local storage
function setBitcoinStatus(){

	$(".our-btc-sentiment").text(localStorage.sentiment_text);
	$(".our-btc-sentiment").css("color", localStorage.sentiment_color);

	$(".our-btc-price").text(localStorage.price_text);
	$(".our-btc-price").css("color", localStorage.price_color);

	$(".our-btc-prediction").text(localStorage.prediction_text);
	$(".our-btc-prediction").css("color", localStorage.prediction_color);
}


// store the predictions obtained from the server to local storage
function updatePredictions(price, sentiment, prediction) {
		if (sentiment > 0.55) {
			localStorage.sentiment_text 	= "POSITIVE";
			localStorage.sentiment_color = "green";
		} else if (sentiment < 0.3) {
			localStorage.sentiment_text 	= "NEGATIVE";
			localStorage.sentiment_color = "red";
		} 
		//
		if (prediction == true) {
			localStorage.price_text 		= price;
			localStorage.price_color 	= "green";
		} else {
			localStorage.price_text 		= price;
			localStorage.price_color 	= "red";			
		}
		//
		if (prediction == true) {
			localStorage.prediction_text 	= "RISE";
			localStorage.prediction_color = "green";
		} else if (prediction == false) {
			localStorage.prediction_text 	= "FALL";
			localStorage.prediction_color = "red";
		} 
}


// scroll to a div on the webpage on button clicked
function scrollToDiv(button_id, div_id){
	$(document).ready(function(){
		$("#"+ button_id).click(function(){
			$('html,body').animate({
				scrollTop: $("#" + div_id).offset().top - 90
			});
		});
	});
}

tweet_count = 1;


function updateTweetStore(tweets){
	displayTweets[1] = createTweetCards(tweets[1]);
	displayTweets[2] = createTweetCards(tweets[2]);
	displayTweets[3] = createTweetCards(tweets[3]);
	displayTweets[4] = createTweetCards(tweets[4]);


}

// update the webpage with sample tweet cards
function updateTweetsOnHomepage(tweets) {
	if (tweet_count == 4) {
		tweet_count = 1;
	}

	document.getElementById('sample-tweet-cards').innerHTML = displayTweets[tweet_count];
	tweet_count+=1;
}


// create sample tweet cards for the webpage
function createTweetCards(tweet) {
	//
	return '<div id="tweet-display-card" class="col-sm-12 animated zoomIn">' +
			'<div id="tweet-display-card-tweet" class="col-sm-9">' +
				'<p><i><b>"'+ tweet.tweet+'"</b></i></p>' + 
			'</div>' + 
			'<div id="tweet-display-card-rating" class="col-sm-3">' +
				'<p><b>' + tweet.rating + '</b></p>' + 
			'</div>' +
		'</div>' +
	'</div>' ; 
}


//
$('#popoverData').popover();
$('#popoverOption').popover({ trigger: "hover" });


// move page location to home
function pushToHome(){
	window.location.href="home.html";	
}


// start up the webapp. gets header predictions from the server
function startUp(){
	getTodaysPredictions();
}
//===========================================================================================




//utils =====================================================================================
//
function getTodaysPredictions() {
	axios.get(server + "/get-todays-predictions")
	  .then(function (response) {
	    updatePredictions(response.data.price, response.data.sentiment, response.data.prediction);
	    setInterval(function(){
	    	pushToHome();
	    },1000)
	})
	  .catch(function (error) {
	    console.log(error);
	});
}

//
function getSampleTweets() {
	axios.get(server + "/get-sample-tweets")
	  .then(function (response) {
	    updateTweetStore(response.data);
	})
	  .catch(function (error) {
	    console.log(error);
	});	
}
//===========================================================================================


//
//getTodaySentimentInformation();
scrollToDiv('find-out-why', 'lstm-heading');
scrollToDiv('about', 'lstm-heading');
setInterval(updateTweetsOnHomepage, 3000);
