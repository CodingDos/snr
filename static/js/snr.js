const inputBox = document.querySelector("input");
const chatWindow = document.querySelector(".chat-window");
const mdFile = document.querySelector(".nav-selector");

document.querySelector("button").addEventListener("click", chatWithAI);

let conversation = [];

function chatWithAI() {
  let mdFileSelected = mdFile.value;
  let userChatMsg = inputBox.value;
  const userChatBubble = document.createElement("div");
  userChatBubble.className = "chat-bubble user-bubble";
  userChatBubble.textContent = userChatMsg;
  chatWindow.appendChild(userChatBubble);
  chatWindow.scrollTop = chatWindow.scrollHeight;

  fetch("chat-with-ai", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_chat_msg: userChatMsg,
      conversation: conversation,
      md_file: mdFileSelected,
    }),
  })
    .then((aiJson) => aiJson.json())
    .then((aiObj) => {
      const aiChatBubble = document.createElement("p");
      aiChatBubble.className = "chat-bubble ai-bubble";
      aiChatBubble.innerHTML = aiObj.ai_msg;
      chatWindow.appendChild(aiChatBubble);
      conversation = aiObj.conversation;
    })
    .catch((error) => console.log("Error: ", error));
  inputBox.value = "";
}
