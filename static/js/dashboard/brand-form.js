document.getElementById('brandForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const name = document.getElementById('name').value;

    fetch('/api/brand/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({name: name})
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert('Create Successful!');
            window.location.href = '/dashboard/brand/list/';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed. Please try again.');
        });
});
