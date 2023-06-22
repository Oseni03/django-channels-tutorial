var socket = new WebSocket('ws://' + window.location.host + '/ws/graph/');
socket.onmessage = function(event) {
    var data = JSON.parse(event.data);
    document.querySelector("#app").innerHTML = data.value;
};