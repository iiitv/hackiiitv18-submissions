
var SITE_TO_TIME_MAP = {}
var focused = true;

setInterval(function() {
  var filters = {active: true, currentWindow: true};

  chrome.tabs.query(filters, function (tabs) {


    if(!tabs || !tabs.length || !focused) return;


    var site = getSiteName(tabs[0].url);
    if (!(site in SITE_TO_TIME_MAP)) {
      SITE_TO_TIME_MAP[site] = 0;
    }
    SITE_TO_TIME_MAP[site] += 5;


    if (SITE_TO_TIME_MAP[site] % 10 === 0) {
      var data = {site: site, time: SITE_TO_TIME_MAP[site]};
      chrome.tabs.sendMessage(tabs[0].id, data, null);

      var opt = {
        type: "basic",
        title: "Time Spent",
        message: "You spent a total of: " + data.time + " seconds on " + data.site,
        iconUrl: "icon.png"
      }

      chrome.notifications.create('spent-on-' + site, opt, function() {
        console.log('notification created');
      });
    }
  });
}, 5000);

function getSiteName(url) {
  var a = document.createElement('a');
  a.href = url;
  return a.hostname;
}


chrome.windows.onFocusChanged.addListener(function (windowId) {
  focused = windowId != -1;
});
