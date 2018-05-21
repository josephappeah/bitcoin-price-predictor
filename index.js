/*============================================================================================================
    										Author : Joseph Appeah;
============================================================================================================*/

// import required modules
var express     = require('express');
var path        = require('path');
var service     = express();

// send utils to client
service.use(express.static('client'));

// load home page
/*============================================================================================================
                                            Launch
============================================================================================================*/
// start the server 
service.listen(8000);
console.log("listening on port : " + 8000);

