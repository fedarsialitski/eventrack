$('div.item-action a').click(function (e) {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});
