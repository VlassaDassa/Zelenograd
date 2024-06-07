// Вывод Price List
$.ajax({
    type: 'GET',
    url: '/get_price_list',
    success: function(response) {
        const data = response.data
        $('#price-list tbody').empty();
        $('.choiceMenu').empty()

        $.each(data, function(index, item) {
            var row = $('<tr>').appendTo('#price-list tbody');
            $('<td>').text(item.name).appendTo(row);
            $('<td>').text(item.unit).appendTo(row);
            $('<td>').text(item.price).appendTo(row);

            $('.choiceMenu').append(
                $('<div>').attr({
                    'class': 'choiceMenuItem'
                }).append(
                    $('<div>').attr({'class': 'choiceMenuItemName'}).text(item.name),
                    $('<div>').attr({'class': 'choiceMenuItemPrice'}).text(item.price),
                )
            )
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



// Увеличение счётчика
$(document).on('click', '.incIco', function(e) {
    const increment = $(this).hasClass('incIco--inc')
    let value_container = $(this).closest('.tableCount').find('.tableCountValue')
    let value = value_container.text()
    if (increment) {
        value_container.text(parseInt(value) + 1)
        const cur_price = parseInt($(this).closest('.tableRow').attr('data-id'))
        $(this).closest('.tableRow').find('.tablePrice').text(cur_price * (parseInt(value) + 1))

        calculating()
        return
    }

    if (parseInt(value) == 0) {
        calculating()
        return
    }

    const cur_price = parseInt($(this).closest('.tableRow').attr('data-id'))
    $(this).closest('.tableRow').find('.tablePrice').text(cur_price * (parseInt(value) - 1))
    value_container.text(parseInt(value) - 1)

    calculating()
})

// Удаление записи
$(document).on('click', '.deleteIcon', function(e) {
    $(this).closest('.tableRow').remove()

    calculating()
})

// Отрытие меню с услугами
$(document).on('click', '.addRowIcon', function(e) {
    $('.choiceMenu').toggle()
})


// Выбор элемента
$(document).on('click', '.choiceMenuItem', function(e) {
    const service_name = $(this).find('.choiceMenuItemName').text()
    const service_price = parseInt($(this).find('.choiceMenuItemPrice').text())
    const parent = $('.calcTableBody')

    var plusIconUrl = $('#staticUrls').data('plus');
    var minusIconUrl = $('#staticUrls').data('minus');
    var trashIconUrl = $('#staticUrls').data('trash');

    var tableRow = $('<div>').addClass('tableRow').attr({'data-id': service_price});
    var tableName = $('<div>').addClass('tableName').text(service_name);
    var tableCount = $('<div>').addClass('tableCount');
    var incIcon = $('<img>').addClass('incIco incIco--inc').attr('src', plusIconUrl).attr('alt', 'Плюс');
    var countValue = $('<p>').addClass('tableCountValue').text('1');
    var decIcon = $('<img>').addClass('incIco incIco--dec').attr('src', minusIconUrl).attr('alt', 'Минус');
    tableCount.append(incIcon, countValue, decIcon);
    var tablePrice = $('<div>').addClass('tablePrice').text(service_price);
    var deleteIcon = $('<img>').addClass('deleteIcon').attr('src', trashIconUrl);
    tableRow.append(tableName, tableCount, tablePrice, deleteIcon);
    parent.children().eq(-2).after(tableRow);

    $('.choiceMenu').toggle()

    calculating()
})


// Подсчёт
function calculating() {
    var sum = 0
    $('.tablePrice').slice(1).each(function() {
        sum += parseInt($(this).text())
    });

    var sumCount = 0
    $('.tableCountValue').each(function() {
        sumCount += parseInt($(this).text())
    });


    $('.totalPriceValue').text(`${sum} рублей`)
    $('.totalCountValue').text(`${sumCount} услуг`)
}