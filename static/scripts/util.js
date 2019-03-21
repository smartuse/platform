// Utility functions

function get_project_path(url) {
    return (url.indexOf('http')<0) ?
      project_path + '/' + url : url;
}
function get_media_type(fmt) {
    if (fmt == 'image') return 'image/png';
    if (fmt == 'png') return 'image/png';
    if (fmt == 'jpg') return 'image/jpeg';
    if (fmt == 'geojson') return 'application/vnd.geo+json';
    if (fmt == 'datapackage') return 'application/vnd.datapackage+json';
    if (fmt == 'embed') return 'application/html';
}

// Full screen mode
function requestFullScreen() {
  element = document.body;
  var requestMethod = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen || element.msRequestFullScreen;
  if (requestMethod) { requestMethod.call(element); }
}
function initFullScreen() {
  $('.fullscreen-button').click(function(e) {
    e.preventDefault();
    if ($(this).hasClass('active')) {
      $(this).removeClass('active').next().removeClass('fullscreen');
      $('html').removeClass('fullscreen');
      // $('.gallery-nav.fixed,.story.fixed').removeClass('hidden');
      // if (document.exitFullscreen) { document.exitFullscreen(); }
    } else {
      // requestFullScreen();
      $(this).addClass('active').next().addClass('fullscreen');
      $('html').addClass('fullscreen');
      // $('.gallery-nav.fixed,.story.fixed').addClass('hidden');
    }
    // Resize the maps
    if (typeof(maps) !== typeof(undefined))
      $.each(maps, function() { this.resize(); });
  });
  $('.share-button').click(function(e) {
    e.preventDefault();
    $('#share').modal('show');
  });
}

// Adjust page sizes
function setStoryLayout() {
  var sh = $(window).height()
         - $('.gallery').height()
         - $('.footer').height()
         - $('site-header').height()
         - 14;
  // $('.story').css('height', sh + 'px');
}
