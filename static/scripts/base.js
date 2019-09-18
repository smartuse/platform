(function(){
  $(window).scroll(function () {
      var top = $(document).scrollTop();
      if(top > 50)
        $('#home > .navbar').removeClass('navbar-transparent');
      else
        $('#home > .navbar').addClass('navbar-transparent');
  });

  $("a[href='#']").click(function(e) {
    e.preventDefault();
  });

  var $button = $("<div id='source-button' class='btn btn-primary btn-xs'>&lt; &gt;</div>").click(function(){
    var html = $(this).parent().html();
    html = cleanSource(html);
    $("#source-modal pre").text(html);
    $("#source-modal").modal();
  });

  // $('.bs-component [data-toggle="popover"]').popover();
  // $('.bs-component [data-toggle="tooltip"]').tooltip();

  $(".bs-component").on('mouseover', function(){
    $(this).append($button);
    $button.show();
  }).on('mouseout', function(){
    $button.hide();
  });

  function cleanSource(html) {
    html = html.replace(/×/g, "&times;")
               .replace(/«/g, "&laquo;")
               .replace(/»/g, "&raquo;")
               .replace(/←/g, "&larr;")
               .replace(/→/g, "&rarr;");

    var lines = html.split(/\n/);

    lines.shift();
    lines.splice(-1, 1);

    var indentSize = lines[0].length - lines[0].trim().length,
        re = new RegExp(" {" + indentSize + "}");

    lines = lines.map(function(line){
      if (line.match(re)) {
        line = line.substring(indentSize);
      }

      return line;
    });

    lines = lines.join("\n");

    return lines;
  }

  $(document).ready(function() {

    // External links in new window
    $('a').each(function() {
      if (typeof this.host === 'undefined') return;
      if (this.host !== window.location.host && !$(this).attr('target')) {
        $(this).attr('target', '_blank');
      }
    });

    // Enable auto fullscreen
    if ($('fullscreen-button').length > 0) initFullScreen();

    // Cookie consent form
    window.cookieconsent.initialise({
      "palette": {
        "popup": { "background": "#008cba" },
        "button": { "background": "#ffffff", "color": "#000000" }
      },
      "content": {
        "message": "Diese Website verwendet Cookies, um Ihnen eine optimale Nutzung unserer Website zu ermöglichen.",
        "dismiss": "Zustimmen",
        "link": "Weitere informationen",
        "href": "/legal"
      }
    });
  });

})();
