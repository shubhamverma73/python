const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const chatMessages = document.getElementById('chatMessages');
const resetBtn = document.getElementById('resetBtn');

function addMessage(role, text, extraClass = '') {
  const wrapper = document.createElement('div');
  wrapper.className = `message ${role} ${extraClass}`.trim();
  wrapper.innerHTML = `
    <div class="avatar">${role === 'user' ? 'You' : 'AI'}</div>
    <div class="bubble"><p>${escapeHtml(text)}</p></div>
  `;
  chatMessages.appendChild(wrapper);
  chatMessages.scrollTop = chatMessages.scrollHeight;
  return wrapper;
}

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

function autoResize() {
  messageInput.style.height = 'auto';
  messageInput.style.height = Math.min(messageInput.scrollHeight, 180) + 'px';
}

messageInput.addEventListener('input', autoResize);
messageInput.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    chatForm.requestSubmit();
  }
});

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const message = messageInput.value.trim();
  if (!message) return;

  addMessage('user', message);
  messageInput.value = '';
  autoResize();

  const typingEl = addMessage('bot', 'Thinking...', 'typing');

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message })
    });

    const data = await res.json();
    typingEl.remove();

    if (!res.ok) {
      addMessage('bot', data.error || 'Something went wrong.');
      return;
    }

    addMessage('bot', data.reply || 'No response received.');
  } catch (err) {
    typingEl.remove();
    addMessage('bot', 'Server error. Make sure Ollama is running and the model is available.');
  }
});

resetBtn.addEventListener('click', async () => {
  await fetch('/reset', { method: 'POST' });
  chatMessages.innerHTML = `
    <div class="message bot">
      <div class="avatar">AI</div>
      <div class="bubble">
        <p>Hello! I am your local Ollama assistant. Ask me anything.</p>
      </div>
    </div>
  `;
});
