// Login function with JSON body
document.getElementById('loginForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/token', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });

        if (!response.ok) throw new Error('Invalid username or password');
        
        const data = await response.json();
        localStorage.setItem('token', data.access_token);
        window.location.href = './fracture_detection.html';
    } catch (error) {
        // document.getElementById('login-error').innerText = error.message;
    }
});

// Register function using JSON body
document.getElementById('registerForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const username = document.getElementById('reg-username').value;
    const password = document.getElementById('reg-password').value;
    const email = document.getElementById('reg-email').value;

    try {
        const response = await fetch('http://127.0.0.1:8000/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username,
                password,
                email
            }),
        });

        if (!response.ok) throw new Error('Registration failed');
        window.location.href = './index.html';

    } catch (error) {
        // document.getElementById('register-error').innerText = error.message;
    }
});

// Event listener for the image upload button
document.getElementById('detectionForm').addEventListener('submit', async function () {
    const fileInput = document.getElementById('image-upload');
    const file = fileInput.files[0];
    const token = localStorage.getItem('token');
    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await fetch('http://localhost:8000/test-fracture', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            body: formData,
        });

        if (!response.ok) throw new Error('Error in detecting fracture');

        const data = await response.json();
        console.log(data);  
        document.getElementById('resultDisplay').innerText = `Prediction: ${data.predicted_class}`;
    } catch (error) {
        document.getElementById('upload-result').innerText = error.message;
    }
});

