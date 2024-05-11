document.getElementById('logoutButton').addEventListener('click', function (event) {
    event.preventDefault();
    fetch('/api/users/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        }
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert('Logout Successful!');
            window.location.href = '/';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Logout failed. Please try again.');
        });
});