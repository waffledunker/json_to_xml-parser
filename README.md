# json_to_xml-parser with sockets
Converting post request(or any type of json stream) JSON values to XML and resending(post request) to desired url with python3


Creating socket-server and listening desired port to recieve data.
Then parse received JSON data to XML
Finally send your xml as HTML POST to desired location.


-> Still needs fixes and optimizations
-> Specify your variables such as host:port and dest_host:port etc. on source.
-> You may need to download some librarys to make it work. (Requests,json2xml etc.)
-> Should not be used in production enviroments yet.
