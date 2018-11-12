var maps = {}, paginationtag = null;

Zepto(function($){

  // Load featured projects
  $('#featured').each(function() {
    var $container = $(this);
    $.getJSON('/api/projects/featured', function(projects) {
      $.each(projects, function() {
        $container.append(
          '<div class="glider" style="background-image:url(\'' + this.screenshot + '\')">' +
            '<a href="/project/' + this.id + '">' +
              '<div class="legend">' +
                '<h4>' + this.title + '</h4>' +
                '<p>' + this.summary + '</p>' +
              '</div>' +
            '</a>' +
          '</div>'
        );
      });
    });
  });

  // Load other projects
  $('#projects').each(function() {
    var $container = $(this);
    $.getJSON('/api/projects', function(projects) {
      $.each(projects, function() {
        $container.append(
        '<div class="col-md-4">' +
          '<a href="/project/' + this.id + '">' +
            '<div class="card text-white mb-3">' +
              '<div class="card-header">' +
                this.title + '</div>' +
              '<div class="card-body">' +
                '<img src="' + this.screenshot + '" width="100" align="left" style="padding-right:1em">' +
                '<p class="card-text">' +
                  this.summary + '</p>' +
              '</div>' +
            '</div>' +
          '</a>' +
        '</div>'
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
    var $cards = $('.project-list .c-card');
    var q = $(this).val().toLowerCase();
    if (q.length < 3) return $cards.show();
    $cards.hide().forEach(function(item) {
      if ($(item).text().toLowerCase().indexOf(q) >= 0)
        $(item).show();
    });
  });

});
