$(document).ready(function () {
    console.log('Document ready');
    //login();
    //fetchItems();

});

function login() {
    fetch('/api/users/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({username: 'test', password: '123456789'})
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));

}

function fetchItems() {
    $.ajax({
        url: '/api/users/',
        type: 'GET',
        success: function (items) {
            var itemsList = $('#items-list');
            itemsList.empty();
            $.each(items, function (index, item) {
                itemsList.append('<li>' + item.username + ' - $' + item.email + '</li>');
            });
        },
        error: function () {
            alert('Error loading items.');
        }
    });
}
