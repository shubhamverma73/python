// Frontend logic for:
// - sending user messages to Flask backend
// - showing bot replies in the chat UI
// - optionally displaying generated SQL and raw SQL results
// - resetting the chat

const chatForm = document.getElementById('chatForm');
const messageInput = document.getElementById('messageInput');
const chatMessages = document.getElementById('chatMessages');
const resetBtn = document.getElementById('resetBtn');
const toggleDebug = document.getElementById('toggleDebug');
const debugPanel = document.getElementById('debugPanel');
const sqlOutput = document.getElementById('sqlOutput');
const resultOutput = document.getElementById('resultOutput');

function escapeHtml(text) {
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

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

toggleDebug.addEventListener('change', () => {
  debugPanel.classList.toggle('hidden', !toggleDebug.checked);
});

chatForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const message = messageInput.value.trim();
  if (!message) return;

  addMessage('user', message);
  messageInput.value = '';
  autoResize();

  const typingEl = addMessage('bot', 'Thinking and querying the database...', 'typing');

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
      if (data.query) sqlOutput.textContent = data.query;
      return;
    }

    addMessage('bot', data.reply || 'No response received.');
    sqlOutput.textContent = data.query || '';
    resultOutput.textContent = data.result || '';
  } catch (err) {
    typingEl.remove();
    addMessage('bot', 'Server error. Check Flask, MySQL, and Ollama setup.');
  }
});

resetBtn.addEventListener('click', async () => {
  try {
    await fetch('/reset', { method: 'POST' });
  } catch (_) {}

  chatMessages.innerHTML = `
    <div class="message bot">
      <div class="avatar">AI</div>
      <div class="bubble">
        <p>Hello! Ask me questions about your MySQL tables.</p>
      </div>
    </div>
  `;

  sqlOutput.textContent = '';
  resultOutput.textContent = '';
});
