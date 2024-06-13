document.addEventListener('DOMContentLoaded', function(){

    const websocketClient = new WebSocket("ws://localhost:12345/");

const message_container = document.querySelector("#message_container");
const message_input = document.querySelector("[name=message_input]");
const message_send_button = document.querySelector("[name=send_message_button]");

// console.log(message_container);


    websocketClient.onopen = function(){
        console.log("cilent connected!");
        // websocketClient.send("hello");

        message_send_button.onclick = function(){
            websocketClient.send(message_input.value);
        };


        // hàm này dùng để lấy message được gửi từ server websocket lên và in vào trang web
        websocketClient.onmessage = function(message){

            const new_message = document.createElement("div");
            new_message.innerHTML = message.data;
            message_container.appendChild(new_message);
            console.log(message.data);
        };
    };


});