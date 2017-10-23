$(document).on('click', 'div.item-action a', function () {
  var href = $(this).attr('href');
  $('form').attr('action', href);
});

$(document).on('click', 'div#artist_sort a', function () {
  var id = $(this).attr('id'),
      activeSort = $('div#artist_sort a.dropdown-item.active'),
      button = document.querySelector('button#artist_button');

  activeSort.removeClass('active');
  $(this).addClass('active');

  $('div.row').addClass('modal');
  $('div.modal.row#' + id).removeClass('modal');

  button.textContent = $(this).text();
});

$(document).on('click', 'div#event_sort a', function () {
  var id = $(this).attr('id'),
      activeSort = $('div#event_sort a.dropdown-item.active'),
      button = document.querySelector('button#event_button');

  activeSort.removeClass('active');
  $(this).addClass('active');

  $('div#' + activeSort.attr('id')).addClass('modal');
  $('div.modal#' + id).removeClass('modal');

  button.textContent = $(this).text();
});

$(document).on('click', 'div#past_event_sort a', function () {
  var id = $(this).attr('id'),
      activeSort = $('div#past_event_sort a.dropdown-item.active'),
      button = document.querySelector('button#past_event_button');

  activeSort.removeClass('active');
  $(this).addClass('active');

  $('div#past_' + activeSort.attr('id')).addClass('modal');
  $('div.modal#past_' + id).removeClass('modal');

  button.textContent = $(this).text();
});

$(document).on('click', 'ul#change_nav li', function () {
  var target = $(this).children().data('target'),
      menuItem = document.querySelector('[href="/profile/' + target + '"]'),
      dropdownItem = document.querySelector('[data-target="' + target + '"]');

  $('a#change_tab.active').removeClass('active');
  $('ul#change_menu.nav li.active').removeClass('active');

  menuItem.parentNode.classList.add('active');
  dropdownItem.classList.add('active');

  if (history.pushState) {
    history.pushState(null, null, target);
  }
  else {
    location.hash = target;
  }
});

$(document).on('click', 'ul#change_menu.nav li', function () {
  var href = $(this).children().attr('href'),
      dropdownItem = $('div#dropdown_menu.dropdown-menu a.dropdown-item');

  if (href.startsWith('/profile/')) {
    var dropdownItems = document.querySelectorAll('div#dropdown_menu.dropdown-menu a.dropdown-item');

    dropdownItem.attr('id', 'change_tab');
    dropdownItem.attr('data-toggle', 'tab');
    dropdownItems.forEach(function(item) {
      item.setAttribute('data-target', item.hash);
    });
  } else {
    var changeTab = $('a#change_tab');

    changeTab.removeAttr('id');
    changeTab.removeAttr('data-toggle');
    changeTab.removeAttr('data-target');
    dropdownItem.removeClass('active');

    location.href = href;
  }
});

$(document).on('click', 'a#change_tab', function () {
  var target = $(this).data('target'),
      menuItem = document.querySelector('[href="/profile/' + target + '"]'),
      dropdownItem = document.querySelector('[data-target="' + target + '"]');

  $('a.nav-link.active').removeClass('active');
  $('[data-target="' + target + '"]').addClass('active');
  $('a#change_tab').removeClass('active');

  if ($(this).hasClass('btn')) {
    $(this).removeClass('active');
  } else {
    $(this).addClass('active');
  }

  $(this).removeAttr('aria-expanded');
  $('ul#change_menu.nav li.active').removeClass('active');

  if (menuItem) {
    menuItem.parentNode.classList.add('active');
  }

  if (dropdownItem) {
    dropdownItem.classList.add('active');
  }

  if (history.pushState) {
    history.pushState(null, null, target);
  }
  else {
    location.hash = target;
  }
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
            count = document.querySelector('span#count_' + data.id),
            comma = document.querySelector('span#comma'),
            text = document.querySelector('span.text-muted#text_' + data.id),
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
          var tab = document.querySelector('div.tab-pane#' + data.id),
              tabRow = document.querySelector('div.row#row_' + data.id),
              tabModal = document.querySelector('div.modal#modal_' + data.id),
              bookmark = document.querySelector('div.tab-pane#bookmarks'),
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
            $('div.modal#modal_' + data.id + ':first').removeClass('modal');
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
