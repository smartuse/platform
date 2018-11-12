var maps = {}, paginationtag = null;

Zepto(function($){

  // Load featured projects
  $('#featured').each(function() {
    $.getJSON('/api/projects/featured', function(projects) {
      $(this).prepend(
        '<div class="glider"></div>'
      );
      $('.c-link--brand a').click(function(e) {
        e.preventDefault();
        window.scrollTo(0, 0);

        var tag = riot.mount('rg-drawer', {
          drawer: {
            header: 'Projects',
            isvisible: true,
            position: 'top',
            items: projects
          }
        });
        tag[0].on('select', function (item) {
          location.href='/project/' + item.id;
        });
        $('rg-drawer .heading').click(function() {
          location.href='/';
        }).css('cursor', 'pointer');
        return false;
      })
    });
  });

  function load_DataPackage(datapackage) {
    var rescount = 0;

    function add_gallery_item(gallery, ii) {
      // gallery.append('<div id="item-'+ii+'" class="control-operator"></div>');
      // gallery.find('.controls').append('<a href="#item-'+ii+'" class="control-button">•</a>');
      if (gallery.attr('fullscreen')) gallery.append('<div class="fullscreen-button"></div>');
      return gallery.append('<figure class="item" />').find('.item:last-child');
    }

    // console.log(datapackage);
    $.each(datapackage.resources, function(i, res) {

      if (res.name.length<2) return;

      container = $('.resource-content').append(
        '<div class="container">'
        + '<div class="gallery" fullscreen=1></div>'
        + '<div class="o-grid" id="' + res.name + '">'
        + '<div class="o-grid__cell--width-20"></div>'
        + '<div class="o-grid__cell"><div class="description"></div></div>'
        + '<div class="o-grid__cell--width-20"></div>'
        + '</div></div>'
      ).find('.container:last-child');
      gallery = container.find('.gallery');
      if (gallery.length === 0) gallery = $('.gallery');
      description = container.find('.description');
      description.append(
        '<div class="resource-header"><a name="anchor-' + rescount + '"></a>'
        + '<h3>' //'<a href="#item-' + rescount + '">'
        // + '<i class="material-icons">layers</i>'
        + (res.title || res.name)
        + '</h3></div>'
      );
      if (res.description.length>1)
        description.append('<p>'+ res.description + '</p>');
      // $('.story-nav ul').append(
      //   '<li><a href="#' + res.name + '">' + (res.title || res.name) + '</a></li>'
      // );

      if (typeof(res.mediatype) == 'undefined')
        res.mediatype = get_media_type(res.format);

      if (res.mediatype == 'application/vnd.datapackage+json') {
        pp = get_project_path(res.path);
        $.getJSON(get_project_path(res.path), function(dp) {
          project_path = pp.substring(0, pp.lastIndexOf('/')+1);
          load_DataPackage(dp);
        });

      } else if (res.mediatype.indexOf('image/')==0) {
        rescount = rescount + 1;
        item = add_gallery_item(gallery, rescount);

        img = item.append('<img id="image-'+rescount+'" />').find('img:last-child');
        imgpath = get_project_path(res.path);
        img.attr('style', 'background-image:url('+imgpath+')');

      } else if (res.mediatype == 'application/html') {
        rescount = rescount + 1;
        item = add_gallery_item(gallery, rescount);

        imgpath = get_project_path(res.path);
        item.append('<iframe id="frame-'+rescount+'" src="' + imgpath + '"/>');

      } else if (res.mediatype == 'application/vnd.geo+json') {
        rescount = rescount + 1;
        item = add_gallery_item(gallery, rescount);

        item.append('<div class="map" id="map-'+rescount+'" />');
        filepath = get_project_path(res.path);

        var lati = 47.38083877331195;
        var long = 8.548545854583836;
        var zoom = 9.28056836461962;

        var map = new mapboxgl.Map({
          container: 'map-' + rescount,
          style: 'mapbox://styles/mapbox/light-v9',
          zoom: zoom,
          center: { lat: lati, lng: long }
        });

        var layer = {
          "id": res.name,
          "type": res.type || "symbol",
          'layout': {}
        };

        if (layer.type == "line")
          layer["paint"] = {
              "line-color": res.color || "#888",
              "line-width": res.linewidth || 3
          };

        if (layer.type == "circle")
          layer["paint"] = {
              "circle-color": res.fillcolor || "#000",
              "circle-radius": res.fillradius || 2,
          };

        if (layer.type == "fill")
          layer["paint"] = {
              "fill-color": res.fillcolor || "#088",
              "fill-opacity": res.fillopacity || 0.8,
          };

        if (layer.type == "symbol")
          layer["layout"] = {
              "icon-image": "{icon}-15",
              "text-field": "{title}",
              "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
              "text-offset": [0, 0.6],
              "text-anchor": "top"
          };

        layer["source"] = {
            "type": "geojson",
            "data": filepath
        };

        // console.log(layer);

        map.on('load', function () {
          map.addLayer(layer);

          if (res.view) {
            map.setCenter({
              lat: res.view.lat  || lati,
              lng: res.view.lng  || long
            });
            map.setZoom(res.view.zoom || zoom);
          }
        });

        maps[rescount] = map;
      } // -geojson
    }); // -each resources

    /*
    if (rescount > 0 && $('rg-pagination').length > 0) {
      // console.log(rescount);
      // gallery.addClass('items-' + rescount);
      paginationtag = riot.mount('rg-pagination', {
        pagination: {
          pages: rescount,
          page: 1
        }
      });
      paginationtag[0].on('page', function (page) {
        if (page < 1) { return paginationtag[0].forward(); }
        if (page > rescount) { return paginationtag[0].back(); }
        location.href="#item-" + page;
        if (maps.hasOwnProperty(page))
          maps[page].resize();
        smoothScroll($('.story'), $('.story').scrollTop()
          + $('a[name="anchor-' + page + '"]').offset().top, 600);
      });
      location.href="#item-1";
    }
    */

    initFullScreen();

  } //-load_DataPackage

  // Load selected project
  if (typeof project_id != 'undefined') {
    $.getJSON('/api/project/' + project_id, load_DataPackage);
  } else if (typeof project_path != 'undefined') {
    $.getJSON('/' + project_path + '/datapackage.json', load_DataPackage);
  }
  // setStoryLayout();
  // $(window).resize(setStoryLayout);

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

  if (typeof mapboxgl !== 'undefined')
    mapboxgl.accessToken = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA';

});
