var init = function() {
  var container = document.createElement('div');
  container.innerHTML =
      '<div class="hidden" id="time-counter-notification">' +
        'You spent a total of: ' +
        '<span id="time-counter-time"></span>' +
        'seconds on <span id="time-counter-site"></span>.' +
      '</div>';
  document.body.appendChild(container);

  chrome.extension.onMessage.addListener(messageRecieved);
};

var messageRecieved = function (data, sender, sendResponse) {
  var notificationEl = document.getElementById('time-counter-notification'),
      timeEl = document.getElementById('time-counter-time'),
      siteEl = document.getElementById('time-counter-site');

  if (data && data.site) {
    timeEl.innerText = data.time;
    siteEl.innerText = data.site;

    notificationEl.className = '';
    setTimeout(function(){notificationEl.className = 'hidden'}, 3000);
  }
};

init();
