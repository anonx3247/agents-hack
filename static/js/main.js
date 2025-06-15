document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const chatForm = document.getElementById('chatForm');
    const messageInput = document.getElementById('messageInput');
    const chatMessages = document.getElementById('chatMessages');
    const coursList = document.getElementById('coursList');
    const exosList = document.getElementById('exosList');

    // Load initial file lists
    loadFiles('cours');
    loadFiles('exos');

    // Handle file upload
    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const formData = new FormData(uploadForm);
        
        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            if (response.ok) {
                alert('File uploaded successfully!');
                loadFiles(formData.get('type'));
                uploadForm.reset();
            } else {
                alert('Error: ' + data.error);
            }
        } catch (error) {
            alert('Error uploading file: ' + error.message);
        }
    });

    // Handle chat messages
    chatForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        const message = messageInput.value.trim();
        if (!message) return;

        // Add user message to chat
        addMessage(message, 'user');
        messageInput.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            if (response.ok) {
                addMessage(data.response, 'assistant');
            } else {
                addMessage('Error: Could not get response from AI', 'assistant');
            }
        } catch (error) {
            addMessage('Error: ' + error.message, 'assistant');
        }
    });

    // Load files for a specific type (cours or exos)
    async function loadFiles(type) {
        try {
            const response = await fetch(`/files/${type}`);
            const files = await response.json();
            
            const list = type === 'cours' ? coursList : exosList;
            list.innerHTML = '';
            
            files.forEach(file => {
                const li = document.createElement('li');
                li.className = 'file-item';
                li.innerHTML = `
                    <span>${file.name}</span>
                    <span class="text-sm text-gray-500">${formatFileSize(file.size)}</span>
                `;
                list.appendChild(li);
            });
        } catch (error) {
            console.error('Error loading files:', error);
        }
    }

    // Add a message to the chat
    function addMessage(text, type) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${type}`;
        messageDiv.textContent = text;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Format file size
    function formatFileSize(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    }

    // Theme toggle logic
    const themeToggle = document.getElementById('themeToggle');
    function setTheme(dark) {
        if (dark) {
            document.body.classList.add('dark');
            localStorage.setItem('theme', 'dark');
        } else {
            document.body.classList.remove('dark');
            localStorage.setItem('theme', 'light');
        }
    }
    // On load, set theme from localStorage
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark' || (savedTheme === null && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        setTheme(true);
    } else {
        setTheme(false);
    }
    themeToggle.addEventListener('click', () => {
        setTheme(!document.body.classList.contains('dark'));
    });
}); 