const sidebar = document.getElementById("chatSidebar");
const toggleBtn = document.getElementById("toggleChat");
const input = document.getElementById("chatInput");
const sendBtn = document.getElementById("sendBtn");
const messages = document.getElementById("chatMessages");
const test = document.getElementById("sendOutput");

/* Toggle sidebar */
toggleBtn.onclick = () => {
    sidebar.classList.toggle("open");
};

/* Send message */
function sendMessage() {
    const text = input.value.trim();
    if (text === "") return;

    const msg = document.createElement("div");
    msg.className = "message";
    msg.textContent = text;

    // bottom aligned chat (older messages moved up)
    messages.prepend(msg);

    input.value = "";
}

/* Send Output to message (test) */
function sendOuput() {
    const text = input.value.trim();
    if (text === "") return;

    const msg = document.createElement("div");
    msg.className = "output-message";
    msg.textContent = text;

    // bottom aligned chat (older messages moved up)
    messages.prepend(msg);

    input.value = "";
}



sendBtn.onclick = sendMessage;
test.onclick = sendOuput;

input.addEventListener("keypress", function(e){
    if(e.key === "Enter"){
        sendMessage();
    }
});