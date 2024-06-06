// Вывод Price List
$.ajax({
    type: 'GET',
    url: '/get_price_list',
    success: function(response) {
        const data = response.data
        $('#price-list tbody').empty();

        $.each(data, function(index, item) {
            var row = $('<tr>').appendTo('#price-list tbody');
            $('<td>').text(item.name).appendTo(row);
            $('<td>').text(item.unit).appendTo(row);
            $('<td>').text(item.price).appendTo(row);
        });
    },

    error: function(xhr, status, error) {
        console.error(xhr.responseText);
    }
});


// Вывод услуг в меню
$.ajax({
    type: 'GET',
    url: '/get_services',
    success: function(response) {
        const data = response.data
        const parent = $('#servicesMenu')  
        parent.empty();

        $.each(data, function(index, item) {
            var path = window.location.pathname;
            var parts = path.split('/');
            var cur_id = parts.pop();

            var url = `/get_service/${item.id}`;
            var text = item.name;
            var listItem = $('<li>').appendTo(parent);
            $('<a>').addClass('dropdown-item').attr('href', url).text(text).appendTo(listItem);
            
            var listItem = $('<li>').addClass('nav-item').appendTo('#navItems');

            if (item.id == cur_id) {
                $('<a>').addClass('nav-link active').attr('href', url).text(text).appendTo(listItem);
            }
            else {
                $('<a>').addClass('nav-link').attr('href', url).text(text).appendTo(listItem);
            }
        });
    },

    error: function(xhr, status, error) {
        console.error(xhr.responseText);
    }
});



// Отправка комментария о проекте
$('#SendCommentBlog').on('click', function(e) {
    e.preventDefault()
    
    // Сбор данных
    const name = $('#name').val()
    const message = $('#comment').val()
    const work_id = $('#work_id').val()

    if (name.length > 0 && message.length > 0) {
        $.ajax({
            url: '/add_comment',
            type: 'POST',
            data: {
                'name': name,
                'message': message,
                'work_id': work_id,
            },
            success: function(response) {
                if (response.success) {
                    alert('Успех');
                } 
                
                else {
                    alert('Неизвестная ошибка - 1');
                }
            },
            error: function() {
                alert('Неизвестная ошибка - 2');
            }
        });
    }
    else {
        alert('Заполните все поля')
    }

    location.reload()
})



// Вывод контактов
// Вывод услуг в меню
$.ajax({
    type: 'GET',
    url: '/get_contacts',
    success: function(response) {
        const data = response.data
        // Header
        $('.collapse').find('p').empty()
        var paragraph = $(`<p>Работаем: 09:00–20:00<br>БЕЗ ВЫХОДНЫХ<br>${data.phone_number.phone_number}</p>`);
        $('.collapse').append(paragraph)

        // Footer
        $('#footerContact').empty()
        var paragraph = $(`<p><i class="fas fa-phone"></i> ${data.phone_number.phone_number} <i class="far fa-envelope ml-2"></i> <a href="mailto:${data.mail.mail}">${data.mail.mail}</a></p>`);
        $('#footerContact').append(paragraph)

        // Contact phone
        $('#contactPhoneNumber').empty()
        var paragraph = `<i class="icon-call-end icons"></i> <strong>Телефон:</strong> ${data.phone_number.phone_number}`
        $('#contactPhoneNumber').append(paragraph)

        // Contact mail
        $('#contactMail').empty()
        var paragraph = `<i class="icon-envelope icons"></i> <strong>Электронная почта:</strong> <br><a href="mailto:${data.mail.mail}">${data.mail.mail}</a>`
        $('#contactMail').append(paragraph)
    },

    error: function(xhr, status, error) {
        console.error(xhr.responseText);
    }
})




