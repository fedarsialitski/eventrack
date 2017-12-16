function Socket(url, icon_url) {
  var socket = new WebSocket(url);

  socket.onopen = function open() {
    console.log('WebSockets connection created.');
  };

  socket.onmessage = function message(event) {
    var data = JSON.parse(event.data);

    notify(data, icon_url);
  };

  if (socket.readyState === WebSocket.OPEN) {
    socket.onopen();
  }
}

function notify(data, icon_url) {
  if ('Notification' in window) {
    var title = data['date'] + ' ' + data['title'],
        options = {
          "body": 'has been changed',
          "icon": icon_url
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
