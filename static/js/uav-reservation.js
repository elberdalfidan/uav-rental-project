$(document).ready(function () {
    console.log('ready datatable')
    $('#reservationsTable').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": {
            "url": "/api/reservation/",
            "type": "GET",
        },
        "columns": [
            {"data": "id"},
            {
                "data": "uav.image",
                "render": function (data, type, row) {
                    return '<img src="' + data + '" width="50" height="50">';
                }
            },
            {"data": "uav.name"},
            {"data": "start_date"},
            {"data": "end_date"},
        ]

    })
})
document.getElementById('reservationForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const formData = {
        uav: document.getElementById('uav').value,
        start_date: document.getElementById('start_date').value,
        end_date: document.getElementById('end_date').value
    };

    fetch('/api/reservation/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken // Assuming csrfToken is stored in cookies
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                alert('Reservation successful!');
                $('#reservationsTable').DataTable().ajax.reload();
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to make reservation. Please try again. ' + error);
        });
});


$('#uav').select2({
    ajax: {
        url: '/api/uav/',
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