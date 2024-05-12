document.getElementById('registerForm').addEventListener('submit', function (event) {
    event.preventDefault()
    const username = document.getElementById('username').value
    const password = document.getElementById('password').value
    const password2 = document.getElementById('password2').value
    const email = document.getElementById('email').value
    const first_name = document.getElementById('first_name').value
    const last_name = document.getElementById('last_name').value

    if (password !== password2) {
        alert('Passwords do not match. Please try again.')
        return
    }

    fetch('/api/users/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            username: username,
            password: password,
            password2: password2,
            email: email,
            first_name: first_name,
            last_name: last_name
        })
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
            alert('Registration Successful!')
            window.location.href = '/login/'
        })
        .catch(error => {
            console.error('Error:', error)
            alert('Registration failed. Please try again.')
        })
});