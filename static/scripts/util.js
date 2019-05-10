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
  if (t.mediatype == "application/vnd.datapackage+json")
    return embedProjectFeature($obj, t.path);
  $obj.append(
    '<a href="' + t.url + '">' +
      '<div class="glider" style="background-image:url(\'' + t.screenshot + '\')">' +
        '<div class="legend">' +
          '<h4>' + t.title + '</h4>' +
          '<p>' + t.summary + '</p>' +
        '</div>' +
      '</div>' +
    '</a>'
  );
}

function embedProjectFeature($obj, tpath) {
  $.getJSON(tpath, function(data) {
    if (!(data.renderings && data.renderings.length > 0
       && data.renderings[0].format == "Embed"))
       return console.error('Unable to load feature: first resource must be an embed.');
    var url = data.renderings[0].path;
    var t = data.data;
    $obj.append(
      '<a href="' + t.url + '">' +
      '<div class="glider" style="background-color:#eee">' +
        '<iframe width="100%" allowtransparency="true" frameborder="0" src="' + url + '"></iframe>' +
        '<div class="legend">' +
          '<h4>' + t.title + '</h4>' +
          '<p>' + t.summary + '</p>' +
        '</div>' +
      '</div>' +
      '</a>'
    );
  })
}

function getProjectCard(t, with_screenshot) {
  if (typeof with_screenshot === 'undefined')
    with_screenshot = true;

  if (t.featured)
    return '' +
      '<div class="col-md-12 project-card featured">' +
        '<a href="' + t.url + '">' +
          '<div class="card mb-12">' +
            '<div class="card-header ">' +
              (!with_screenshot ? '' :
                '<img src="' + t.thumbnail + '">') +
              '<div class="card-text">' +
                '<b class="title">' + t.title + '</b>' +
                // (typeof t.organisation === 'undefined' ? '' :
                //   '<p class="organisation">' + t.organisation + '</p>') +
                '<p class="summary">' + t.summary + '</p>' +
              '</div>' +
            '</div>' +
          '</div>' +
        '</a>' +
      '</div>';

    return '' +
      '<div class="col-md-4 project-card">' +
        '<a href="' + t.url + '">' +
          '<div class="card mb-3">' +
            '<div class="card-header ">' +
              (!with_screenshot ? '' :
                '<img src="' + t.thumbnail + '" width="100" align="left" style="padding-right:1em">') +
              '<b class="title">' + t.title + '</b>' +
              '<p class="card-text">' + t.summary + '</p>' +
              // (typeof t.organisation === 'undefined' ? '' :
              //   '<small class="organisation">' + t.organisation + '</small>') +
            '</div>' +
          '</div>' +
        '</a>' +
      '</div>';
}
