  var http = require('http').createServer(handler); //require http server, and create server with function handler()
  var fs = require('fs'); //require filesystem module
  var io = require('socket.io')(http) //require socket.io module and pass the http object (server)
  var pshell = require('python-shell');

  var motRight = new pshell('s1.py', { mode: 'json '});
  var motLeft = new pshell('s2.py', { mode: 'json '});
  var camMot = new pshell('camMot.py',{model: 'json'});

  var lightvalue = 0;

  http.listen(3000); //listen to port 8080

  function handler (req, res) { //create server
    fs.readFile(__dirname + '/public/index.html', function(err, data) { //read file index.html in public folder
      if (err) {
          res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
          return res.end("404 Not Found");
        } 
      res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
      res.write(data); //write data from index.html
      return res.end();
    });
  }

  io.sockets.on('connection', function (socket) {// WebSocket Connection
     //static variable for current status
    socket.on('rightMotor', function(data) { //get light switch status from client
              // lightvalue = data 
              console.log("right motor")
              console.log(data);    
              if (data == "1") {
                motRight.send("F");
              } else if (data == "0") {
                motRight.send("stop");
              } else if (data == "2") {
                motRight.send("B");
              }
            });

    socket.on('leftMotor', function(data) { //get light switch status from client
              console.log("left motor")
              console.log(data);    
              if (data == "1") {
                motLeft.send("B");
              } else if (data == "0") {
                motLeft.send("stop");
              } else if (data == "2") {
                motLeft.send("F");
              }
            });
    socket.on('camMot', function(data) {
    	    console.log("camera Motor")
	    console.log(data);
	    camMot.send(data)
    });

    socket.on('shutdown', function(data) { //get light switch status from client     
      motRight.send("shutdown");
      motLeft.send("shutdown");
    });
    
  });


