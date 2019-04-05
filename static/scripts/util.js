// Utility functions

function get_project_path(url, canonical_url) {
    pp = (canonical_url || PROJECT_ROOT || '');
    if (typeof url === 'undefined') return pp;
    return (url.indexOf('http')<0) ?
      pp + '/' + url : url;
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


function getProjectFeature($obj, t) {
  $obj.append(
    '<div class="glider" style="background-image:url(\'' + t.screenshot + '\')">' +
      '<a href="' + t.url + '">' +
        '<div class="legend">' +
          '<h4>' + t.title + '</h4>' +
          '<p>' + t.summary + '</p>' +
        '</div>' +
      '</a>' +
    '</div>'
  );
}

function getProjectCard(t, with_screenshot) {
  if (typeof with_screenshot === 'undefined')
    with_screenshot = true;
  return '' +
  '<div class="col-md-6 project-card">' +
    '<a href="' + t.url + '">' +
      '<div class="card mb-5">' +
        '<div class="card-header ">' +
          (with_screenshot && t.featured ?
            '<img src="' + t.thumbnail + '" width="100%">'
            : '') +
          '<b class="title">' + t.title + '</b>' +
          (typeof t.organisation === 'undefined' ? '' :
          '<div class="organisation">' + t.organisation + '</div>') +
          '</div>' +
        (t.featured ? '' :
        '<div class="card-body">' +
          (with_screenshot && !t.featured ?
            '<img src="' + t.thumbnail + '" width="100" align="left" style="padding-right:1em">'
            : '') +
          '<p class="card-text">' + t.summary + '</p>' +
        '</div>') +
      '</div>' +
    '</a>' +
  '</div>'
}
