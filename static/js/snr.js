const inputBox = document.querySelector("input");

inputBox.addEventListener("change", chatWithAI);

let conversation = []

function  chatWithAI(){
    let userChatMsg = inputBox.value;
    const userChatBubble = document.createElement("div");


    fetch("chat-with-ai", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({
            user_chat_msg: userChatMsg,
            conversation: conversation
        })
    })
    .then(aiJson => aiJson.json())
    .then(aiObj => {
        
    })
}