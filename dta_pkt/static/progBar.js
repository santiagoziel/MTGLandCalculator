var socket = io();

socket.on('user acknowledgment', function(message){
console.log("client", message);
});

socket.on('updateBar', function(message){
const updateMessage = document.getElementById('updateMessage')
console.log(updateMessage);
bar = document.getElementById("progresBar")
bar.value = message['status']
updateMessage.innerHTML = `${message['message']}`
});

const formElement = document.querySelector("form");

elem = document.getElementById('submitbutton');


elem.onclick = function(){
  elem.onclick=null;
  const progBar = document.createElement("progress")
  progBar.setAttribute("id", "progresBar");
  progBar.setAttribute("value", "0");
  progBar.setAttribute("max", "100");

  formElement.appendChild(progBar);

  const updatePlace = document.createElement("div")
  updatePlace.setAttribute("class", "container")
  document.body.appendChild(updatePlace)

  updatePlace.insertAdjacentHTML(
    'beforeend',
  `<h3 class="updateMessage" id="updateMessage"> Reading File </h3>`,
);

  const request = new XMLHttpRequest();
  request.open("POST", "/");
  request.onreadystatechange = function() {
     if (request.readyState === 4) {
       location.href = request.response;
     }
   }
  request.send(new FormData(formElement));
};
