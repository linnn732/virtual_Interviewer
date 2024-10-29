const express = require('express');
const app = express();
const fs = require('fs');
const https = require('https');
const { json } = require('body-parser');

const PORT = 3000;


var WebSocketServer = require('ws').Server;

const SERVER_CONFIG = {
    key: fs.readFileSync('ssl/private.key'),
    cert: fs.readFileSync('ssl/merge.crt')
};

const httpsServer = https.createServer(SERVER_CONFIG, app);

httpsServer.listen(PORT, () => console.log(`Listening on https://concall.54ucl.com:${PORT}`));


const wss = new WebSocketServer({ server: httpsServer });

app.use('/public',express.static('public'));

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
})

app.post('/record', function(req, res){

    res.sendFile(__dirname + '/record.html');

})
