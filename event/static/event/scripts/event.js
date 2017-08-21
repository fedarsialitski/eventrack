$(document).on('click', 'div.item-action a', function () {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});

$(document).on('click', '.btn-favorite', function () {
  var url = $(this).data('url'),
      button = $(this).children('i'),
      className = button[0].classList[1];

  $.ajax({
    url: url,
    dataType: 'json',
    success: function () {
      switch (className) {
        case 'fa-star':
          button.removeClass('fa-star');
          button.addClass('fa-star-o');
          break;
        case 'fa-star-o':
          button.removeClass('fa-star-o');
          button.addClass('fa-star');
          break;
      }
    }
  });
});
