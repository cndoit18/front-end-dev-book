let socket;

function init(url) {
    socket = new WebSocket(url);
    console.log('connecting...');
}

function registerOpenHandler(handlerFunction) {
    socket.onopen = () => {
        console.log('open');
        handlerFunction();
    };
}
function registerMessageHandler(handlerFunction) {
    socket.onmessage = (e) => {
        e.data.text().then((text) => {
            console.log('message', text);
            let data = JSON.parse(text);
            handlerFunction(data);
        });
    };
}

function sendMessage(payload) {
    socket.send(JSON.stringify(payload));
}

export default {
    init,
    registerOpenHandler,
    registerMessageHandler,
    sendMessage
};
