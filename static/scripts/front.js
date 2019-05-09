var maps = {}, paginationtag = null;

jQuery(function($){

  // Load the gallery
  if ($('#featured').length) {
    $.getJSON('/api/projects/by/top', function(projects) {
      var $container = $('#featured');
      $.each(projects, function() {
        getProjectFeature($container, this);
      });
    });
  }

  // Load project categories
  function listProjects(projects) {
    var $container = $('#home-projects');
    $.each(projects, function() {
      if (!this.category) return;
      var $cat = $container.find('[project-category="' + this.category + '"]');
      if ($cat.length === 1) {
        $cat.addClass('project-list');
        $cat.append(getProjectCard(this));
      } else {
        console.warn('Category not found', this.category);
      }
    });
  }

  // Load all project categories
  $('#home-projects [project-category]').each(function() {
    var p_type = $(this).attr('project-category');
    $.getJSON('/api/projects/by/' + p_type, listProjects);
  });

  // Load search results
  $('#projects-search').each(function() {
    function urldecode(str) { return decodeURIComponent((str+'').replace(/\+/g, '%20')); }
    var $container = $(this).addClass('project-list');
    var query = document.location.search;
    var url = '/api/projects/search' + query;
    if (query == '?all') {
      url = '/api/projects/all'; query = '';
    }
    $('input.search').val(urldecode(query.replace('?q=', '')));
    $.getJSON(url, function(projects) {
      if (projects.length) $container.empty();
      $.each(projects, function() {
        $container.append(
          getProjectCard(this)
        );
      });
      $container.show();
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
