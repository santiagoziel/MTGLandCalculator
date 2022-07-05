var socket = io();
//when new user conects it updates list of abailable users
socket.on('user acknowledgment', function(message){
console.log("client", message);
});
