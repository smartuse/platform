var maps = {}, paginationtag = null;

jQuery(function($){

  // Load the gallery
  if ($('#featured').length)
  $.getJSON('/api/projects/featured', function(projects) {

    $('#featured').each(function() {
      var $container = $(this);
      $.each(projects, function() {
        getProjectFeature($container, this);
      });
    });

  });

  // Load Labs project categories
  $.getJSON('/api/projects', function(projects) {

    $('#projects').each(function() {
      var $container = $(this).addClass('project-list');
        $.each(projects, function() {
          if (this.featured)
            $container.prepend(getProjectCard(this));
          else
            $container.append(getProjectCard(this));
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
/*
  $('input.search').on('input', function() {
    var $cards = $('#projects .project-card');
    var q = $(this).val().toLowerCase();
    if (q.length < 3) return $cards.show();
    $cards.hide().forEach(function(item) {
      if ($(item).text().toLowerCase().indexOf(q) >= 0)
        $(item).show();
    });
  });
*/
});
