$(document).on('click', 'div.item-action a', function () {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});

$(document).on('click', '.btn-favorite', function (e) {
  e.stopImmediatePropagation();

  var id = $(this).data('id'),
      url = $(this).data('url'),
      button = $(this).children('i'),
      className = button[0].classList[1],
      pathName = window.location.pathname;

  $.ajax({
    url: url,
    dataType: 'json',
    success: function (data) {
      if (pathName === '/profile/') {
        var elements = document.querySelectorAll("#" + id);

        elements.forEach(function(node){
          node.parentNode.removeChild(node);
        });
      } else {
        var selector = '#' + id + ' span.item-meta-stats',
            count = document.querySelector(selector),
            countClass = $(selector).hasClass('text-xs');

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

        if (data.count) {
          if (countClass) {
              count.innerHTML = '<i class="fa fa-star text-muted"></i> ' + data.count;
          } else {
              count.innerHTML = data.count;
          }
        } else {
          count.innerHTML = '&nbsp';
        }
      }
    }
  });
});
