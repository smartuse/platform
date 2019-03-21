var maps = {}, paginationtag = null;

jQuery(function($){

  function getProjectFeature($obj, t) {
    $obj.append(
      '<div class="glider" style="background-image:url(\'' + this.screenshot + '\')">' +
        '<a href="/project/' + this.id + '">' +
          '<div class="legend">' +
            '<h4>' + this.title + '</h4>' +
            '<p>' + this.summary + '</p>' +
          '</div>' +
        '</a>' +
      '</div>'
    );
  }

  function getProjectCard(t, with_screenshot) {
    if (typeof with_screenshot === 'undefined')
      with_screenshot = true;
    return '' +
    '<div class="col-md-4 project-card">' +
      '<a href="/project/' + t.id + '">' +
        '<div class="card mb-3">' +
          '<div class="card-header ">' +
            '<b class="title">' + t.title + '</b>' +
            (typeof t.organisation === 'undefined' ? '' :
            '<div class="organisation">' + t.organisation + '</div>') +
            '</div>' +
          '<div class="card-body">' +
            (with_screenshot ?
              '<img src="' + t.thumbnail + '" width="100" align="left" style="padding-right:1em">'
              : '') +
            '<p class="card-text">' +
              t.summary + '</p>' +
          '</div>' +
        '</div>' +
      '</a>' +
    '</div>'
  }

  // Load featured projects
  $('#featured').each(function() {
    var $container = $(this);
    $.getJSON('/api/projects/featured', function(projects) {
      $.each(projects, function() { getProjectFeature($container, this); });
    });
  });

  // Load main projects
  $('#projects-featured').each(function() {
    var $container = $(this).addClass('project-list');
    $.getJSON('/api/projects/featured', function(projects) {
      $.each(projects, function() {
        $container.append(
          getProjectCard(this, false)
        );
      });
    });
  });

  // Load other projects
  $('#projects').each(function() {
    var $container = $(this).addClass('project-list');
    $.getJSON('/api/projects', function(projects) {
      $.each(projects, function() {
        $container.append(
          getProjectCard(this)
        );
      });
    });
  });

  // Load search results
  $('#projects-search').each(function() {
    function urldecode(str) { return decodeURIComponent((str+'').replace(/\+/g, '%20')); }
    $('input.search').val(urldecode(document.location.search.replace('?q=', '')));
    var $container = $(this).addClass('project-list');
    $.getJSON('/api/projects/search' + document.location.search, function(projects) {
      $.each(projects, function() {
        $container.append(
          getProjectCard(this)
        );
      });
    });
  });

  /*
        each project in projects
          .c-card
            a(href='/project/{{ project.id }}')
              .c-card__header
                img.project-thumb(src='{{ project.thumb() }}',align='left')
                h2.c-heading
                  =project.title
                each user in project.users
                  span= user.organisation
              if project.summary
                .c-card__body
                  .c-paragraph
                    =project.summary
*/

  // Interactive search
  $('input.search').on('input', function() {
    var $cards = $('#projects .project-card');
    var q = $(this).val().toLowerCase();
    if (q.length < 3) return $cards.show();
    $cards.hide().forEach(function(item) {
      if ($(item).text().toLowerCase().indexOf(q) >= 0)
        $(item).show();
    });
  });

});
