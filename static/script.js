function sendMessage() {
  const userInput = document.getElementById('user-input').value;
  fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: 'message=' + encodeURIComponent(userInput)
  })
  .then(response => response.json())
  .then(data => {
      const chatBox = document.getElementById('chat-box');
      chatBox.innerHTML += `<div class="user-msg">${userInput}</div>`;
      chatBox.innerHTML += `<div class="bot-msg">${data.response}</div>`;
      document.getElementById('user-input').value = '';
  });
}
