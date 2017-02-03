Group Details:
			  Prabhanjan SK - 1pi14is036
			  Prajwal MR - 1pi14is037
			  Shashank TD - 1pi14is060

Execution of the program:
						   Thro command line- python client-asn1.py -w url -O outputFileName.format
						   example : python client-asn1.py -w https://skprabhanjan.github.io/aboutme/stylesheets/github-dark.css -O output.txt
Working:
		The program uses the file system to store the already accessed url's as cache and then later retrive the cached/stored value sfrom the local file system if exixts and the response returns a 304 status,if the url is not accessed before and is not cached then the response is taken from the url and then cached and is later used for further retrival when this url is acccessed once more. A directory called cache is created first and then a file called map.txt is created which stores a 32-bit random number and the encrypted value of the url(encryption done using sha1) and then a text file with that random number is created that stores the headers that the response sent and the data, When we access the url first time the response returns a header called Last-Modified which is used as request header If-Modified-Since in the further requests which wil lead to a status code 304,On getting a status code of 304 the reponse that is stored in the cache of that url is retirvied and then written to the output file, if the response is a 200 then the response is cached and stored for further use
Challenges Faced:
					Coming up with algorithm to actually map each url to a random number and then store that url's headers and data, Then we faced one more realy challening issue where we used to read line by line to see if the url was already used, But we faced an issue when the url was more than a specific length then it used to take two line and therefore the results were not as expected, So we up with a solution to encrypt the url using sha1 that encryptes this url and returns a secure hashed value and therefore however long the url is, it is eventually converted to a constant encrypted value and when a url is accessed we encrypt this once again and check if both the encrypted values are same and if we return the txt file name that contains this url's headers and data
	Example:	
			testurl -> https://skprabhanjan.github.io/aboutme/stylesheets/github-dark.css
			outputfile -> result.txt
			command -> python client-asn1.py -w https://skprabhanjan.github.io/aboutme/stylesheets/github-dark.css -O result.txt
			So the response on first attempt will be 200 and a map.txt and a coressponding random_number.txt is created that houses the headers sent by this url and then a separating chararcter followed by the response data that was received.
			Next time access to this url would search the map.txt to see if this was already accessed and if it returns the file name of the file where its headers and data are stored and in the second request onwards the If-Modified-Since headers are set to the Last-Modified header that was recieved in the first  response and therefore the second request onwards if there was no change in the file the repsonse status would be 304 and the data is retrived from the local file that stored this data for this specific url and therefore serves the purpose.
Test Url's:
           1) https://www.google.com/textinputassistant/tia.png 

           2) https://apis.google.com/_/scs/abc-static/_/js/k=gapi.gapi.en.67eqDUukfqs.O/m=gapi_iframes,googleapis_client,plusone/rt=j/sv=1/d=1/ed=1/rs=AHpOoo8OHf8cPYJ8tiz0hBBMUN5_oj6oBg/cb=gapi.loaded_0
 
           3) https://www.facebook.com/rsrc.php/v3/yn/r/Fn0ud8qGK_Q.css

           4) https://www.facebook.com/rsrc.php/v3/yE/r/uqWZrDdEiFq.css

           5) https://www.facebook.com/rsrc.php/v3/y5/r/_f7nU8Zyvqq.js

           6) https://www.facebook.com/rsrc.php/v3/yg/r/0xaZKbjJdTW.js

           7) http://pes.edu/wp-content/plugins/js_composer/assets/lib/waypoints/waypoints.min.js?ver=4.6

           8) http://pes.edu/wp-content/themes/university/style.css?ver=4.0.12

           and finally the longesturl

           9) http://thelongestlistofthelongeststuffatthelongestdomainnameatlonglast.com/wearejustdoingthistobestupidnowsincethiscangoonforeverandeverandeverbutitstilllookskindaneatinthebrowsereventhoughitsabigwasteoftimeandenergyandhasnorealpointbutwehadtodoitanyways.html
