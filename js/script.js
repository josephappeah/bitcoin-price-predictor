server 			= "http://localhost:3000";
displayTweets 	= [];



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
				scrollTop: $("#" + div_id).offset().top
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
getTodaySentimentInformation();
scrollToDiv('find-out-why', 'sentiment-analysis');
setInterval(blink_text, 1000);