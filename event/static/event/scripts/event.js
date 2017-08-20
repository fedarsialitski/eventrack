$(document).on('click', 'div.item-action a', function () {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});

$(document).on('click', '.btn-favorite', function () {
  var url = $(this).data('url');

  $.ajax({
    url: url,
    dataType: 'json',
    success: function () {
    }
  });
});