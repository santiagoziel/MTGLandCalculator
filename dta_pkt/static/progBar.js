var socket = io();

socket.on('user acknowledgment', function(message){
console.log("client", message);
});

socket.on('updateBar', function(message){
console.log(message);
bar = document.getElementById("progresBar")
bar.value = message
});

const formElement = document.querySelector("form");

elem = document.getElementById('submitbutton');

elem.onclick = function(){
  const progBar = document.createElement("progress")
  progBar.setAttribute("id", "progresBar");
  progBar.setAttribute("value", "0");
  progBar.setAttribute("max", "100");

  document.body.appendChild(progBar);
  const request = new XMLHttpRequest();
  request.open("POST", "/");
  request.onreadystatechange = function() {
     if (request.readyState === 4) {
       location.href = request.response;
     }
   }
  request.send(new FormData(formElement));
};
