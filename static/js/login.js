document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/api/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({username: username, password: password})
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert('Login Successful!');
            window.location.href = '/';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Login failed. Please try again.');
        });
});
