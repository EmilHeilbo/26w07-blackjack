var ws = null;

function getToken() {
  const cookies = document.cookie.split("; ");
  const tokenCookie = cookies.find((c) => c.trim().indexOf("token=") === 0);
  return tokenCookie ? tokenCookie.split("=")[1] : null;
}

function setToken(token) {
  document.cookie = `token=${token}; path=/; SameSite=Lax`;
}

function connect(event) {
  // Generate auth token if it doesn't already exist in a cookie
  if (getToken() == null) {
    fetch(`/api/get-uuid`)
      .then((response) => response.text())
      .then((uuid) => setToken(uuid));
  }

  ws = new WebSocket("/ws");
  ws.onmessage = function (event) {
    var messages = document.getElementById("messages");
    var message = document.createElement("li");
    var content = document.createTextNode(event.data);
    message.appendChild(content);
    messages.appendChild(message);
  };
  event.preventDefault();
}

function disconnect(event) {
  if (ws) {
    ws.close();
    ws = null;
  }
}

function sendMessage(event) {
  var input = document.getElementById("messageText");
  ws.send(input.value);
  input.value = "";
  event.preventDefault();
}
