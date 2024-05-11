document.getElementById('uavForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData();
    formData.append('name', document.getElementById('name').value);
    formData.append('model', document.getElementById('model').value);
    formData.append('weight', document.getElementById('weight').value);
    formData.append('brand', document.getElementById('brand').value);
    formData.append('category', document.getElementById('category').value);
    formData.append('image', document.getElementById('image').files[0]);

    fetch('/api/uav/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert('Create Successful!');
            //window.location.href = '/dashboard/uav/list/';
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed. Please try again.');
        });
});

$('#brand').select2({
    ajax: {
        url: '/api/brand/',
        dataType: 'json',
        data: function (params) {
            return {
                search: params.term
            }
        },
        processResults: function (data) {
            return {
                results: data.data.map(function (item) {
                    return {
                        id: item.id,
                        text: item.name
                    }
                })
            }
        }
    }
});


$('#category').select2({
    ajax: {
        url: '/api/category/',
        dataType: 'json',
        data: function (params) {
            return {
                search: params.term
            }
        },
        processResults: function (data) {
            return {
                results: data.data.map(function (item) {
                    return {
                        id: item.id,
                        text: item.name
                    }
                })
            }
        }
    }
});
