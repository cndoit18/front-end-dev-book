var http = require('http');
var fs = require('fs');
var extract = require('./extract');

var handlerError = function (err, res) {
    res.writeHead(404);
    res.end();
};

var server = http.createServer(function (req, res) {
    console.log('Responding to a request.');
    var filePath = extract(req.url);
    fs.readFile(filePath, function (err, data) {
        if (err) {
            handlerError(err, res);
            return;
        }
        res.setHeader('Content-Type', 'text/html');
        res.end(data);
    });
});
server.listen(3000);
