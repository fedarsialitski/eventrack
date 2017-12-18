function Socket(url, icon_url) {
  var socket = new WebSocket(url);

  socket.addEventListener('open', function () {
    console.log('WebSockets connection created.');
  });

  socket.addEventListener('message', function (event) {
    var data = JSON.parse(event.data),
        title = data['date'] + ' ' + data['title'],
        body = 'has been changed';

    notify(title, body, icon_url);
  });
}

function notify(text, body, icon) {
  if ('Notification' in window) {
    var title = text,
        options = {
          "body": body,
          "icon": icon
        };

    switch (Notification.permission) {
      case 'default':
        Notification.requestPermission().then(function (permission) {
          if (permission === 'granted') {
            new Notification(title, options);
          }
        });
        break;
      case 'granted':
        new Notification(title, options);
        break;
    }
  }
}
