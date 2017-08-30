$(document).on('click', 'div.item-action a', function () {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});

$(document).on('click', 'div.item-action a#edit_profile', function () {
  var activeTab = $('div.tab-pane.active'),
      activeNav = $('a.nav-link.active'),
      profileTab = $('div#tab_profile.tab-pane'),
      profileNav = $('[data-target="#tab_profile"]');

  activeNav.removeClass('active');
  activeTab.removeClass('active');
  activeTab.attr('aria-expanded', 'false');

  profileNav.addClass('active');
  profileTab.addClass('active');
  profileTab.attr('aria-expanded', 'true');
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
          var tab = document.querySelector('div.tab-pane#tab_' + data.id),
              tabRow = document.querySelector('div.row#' + data.id),
              tabModal = document.querySelector('div.modal#' + data.id),
              bookmark = document.querySelector('div.tab-pane#tab_bookmark'),
              bookmarkRow = document.querySelector('div.row#bookmark_' + data.id),
              bookmarkModal = document.querySelector('div.modal#bookmark_' + data.id);

          if (text) {
            text.remove();
          }

          if (count) {
            count.remove();
          }

          if (comma) {
            comma.remove();
          }

          if (bookmark && bookmarkRow && bookmarkModal) {
            bookmark.replaceChild(bookmarkModal.cloneNode(true), bookmarkRow);
            $('div.modal#bookmark_' + data.id + ':first').removeClass('modal');
          }

          if (tab && tabRow && tabModal) {
            tab.replaceChild(tabModal.cloneNode(true), tabRow);
            $('div.modal#' + data.id + ':first').removeClass('modal');
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
