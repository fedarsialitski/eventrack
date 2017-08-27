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
        var elements = document.querySelectorAll("#" + id),
            count = document.querySelector('span#' + data.id),
            comma = document.querySelector('span#comma'),
            text = document.querySelector('span.text-muted#' + data.id),
            dataCount;

        elements.forEach(function(node){
          node.parentNode.removeChild(node);
        });

        switch (data.id) {
          case 'events':
            dataCount = data.event_count;
            break;
          case 'artists':
            dataCount = data.artist_count;
            break;
        }

        if (dataCount) {
          count.textContent = dataCount;
        } else {
          text.remove();
          count.remove();

          if (comma) {
            comma.remove();
          }
        }
      } else {
        var selector = '#' + id + ' span.item-meta-stats',
            userCount = document.querySelector(selector),
            userCountClass = $(selector).hasClass('text-xs');

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

        if (data.user_count) {
          if (userCountClass) {
            userCount.innerHTML = '<i class="fa fa-star text-muted"></i> ' + data.user_count;
          } else {
            userCount.innerHTML = data.user_count;
          }
        } else {
          userCount.innerHTML = '&nbsp';
        }
      }
    }
  });
});
