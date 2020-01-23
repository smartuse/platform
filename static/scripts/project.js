var maps = {}, paginationtag = null, project_path = '';

jQuery(function($){

  function load_DataPackage(datapackage, top_container, canonical_url) {
    var rescount = 0;
    if (typeof canonical_url !== 'string') canonical_url = project_path;

    function add_gallery_item(container, ii) {
      var gallery = $('<div class="gallery" fullscreen=1></div>').prependTo(container);
      if (gallery.length === 0) gallery = $('.gallery');
      if (gallery.length === 0) return null;
      // gallery.append('<div id="item-'+ii+'" class="control-operator"></div>');
      // gallery.find('.controls').append('<a href="#item-'+ii+'" class="control-button">•</a>');
      gallery.append('<div title="Share" class="side-button share-button"></div>');
      if (gallery.attr('fullscreen'))
        gallery.append('<div title="Vollbild" class="side-button fullscreen-button"></div>');
      return $('<figure class="item" />').appendTo(gallery);
    }

    function add_rendering_summary(res) {
      return $('.rendering-summary').append(
        '<div class="list-group-item list-group-item-action flex-column align-items-start">' +
          '<div class="d-flex w-100 justify-content-between">' +
            '<h5 class="mb-1">' +
              (res.name || res.title) +
            '</h5>' +
            '<div role="group" class="download-buttons btn-group">' +
              '<small class="btn btn-sm download-format">' + (res.format || res.mediatype || '') + '</small>' +
              '<a type="button" href="' + get_project_path(res.path, canonical_url) + '" ' +
              (res.mediatype && res.mediatype.indexOf('application') == 0 ?
                'class="btn btn-primary btn-sm">Anschauen</a>' :
                'download class="btn btn-primary btn-sm">Herunterladen</a>') +
            '</div>' +
          '</div>' +
          (res.sources ? get_data_sources(res.sources) : '') +
        '</div>'
      );
    }

    function get_data_sources(sources) {
      return '<ul class="res-sources">' +
        $.map(sources, function(x) { return '<li>' +
          (x['organisation'] ?
            '<img src="' + x['organisation']['logo'] + '">' :
            '<img src="/img/usericon.png">') +
          '<a href="' + x['path'] + '">' +
            x['title'] + '</a>' +
          '<fmt>' + x['format'] + '</fmt>' +
          (x['organisation'] ?
            '<p><a class="org" href="' + x['organisation']['url'] + '" target="_blank">' +
              x['organisation']['name'] + '</a></p>' : '') +
          (x['license'] ?
            '<p><a class="license" href="' + x['license']['path'] + '" target="_blank">' +
              x['license']['name'] + '</a></p>' : '') +
          '</li>'
        }).join('\n')
      + '</ul>';
    }

    if (datapackage.data)
      add_rendering_summary(datapackage.data);

    // console.log(datapackage);
    $.each(datapackage.renderings, function(i, res) {

      if (!(res.name || res.title)) return;

      if (typeof(top_container) == 'object') {
        container = top_container;
      } else {
        var $renderingContent = $('.rendering-content');
        container = $renderingContent.append(
          '<div class="rendering-container">'
          + '<div class="container row justify-content-md-center">'
            + '<div class="description col-md-8"></div>'

            + '<div class="rendering-datasets col-md-2">'

            + (typeof res.author !== 'undefined' ?
              '<p class="res-author">' + res.author + '</p>' : '')

            + (typeof res.sources !== 'undefined' && res.sources.length > 0?
                '<b>' + 'Datengrundlage' + '</b>' +
                get_data_sources(res.sources) : '')

            + '</div>'

          + '</div>'
        + '</div>'

        ).find('.rendering-container:last-child').find('.container');

        summary = add_rendering_summary(res);
      }

      var count = rescount + 1;
      container.before(
        '<div class="rendering-header"><a name="anchor-' + count + '"></a>'
        + '<div class="rendering-counter">' + count + '</div>'
        //'<a href="#item-' + rescount + '">'
        // + '<i class="material-icons">layers</i>'
        + '<h2>' + (res.title || res.description) + '</h2>'
        + '</div>'
      );

      description = container.find('.description');
      if (res.title && res.description && res.description.length>1) {
        description.append(res.description);
      } else {
        // Remove description container if unused
        description.next().removeClass('col-md-3').addClass('col-md-12');
        description.remove();
      }

      datasets = container.find('.rendering-datasets');
      if (res.doc_url && res.doc_url.length>0)
        datasets.append('<p class="doc_url"><a href="' + res.doc_url + '">&#128366; Details</a></p>');
      if (res.pipeline && res.pipeline.length>0) {
        datasets.append('<div class="mermaid" id="mermaid' + res.id + '"></div>');
        res_id = (res.id || res.name || res.title.replace(' ', '-'));
        var graph = mermaid.render('mermaid' + res_id, 'graph LR;' + res.pipeline,
          function (svgCode, bindFunctions) { $('#mermaid' + res_id).html(svgCode); });
      }

        // console.log(res);

      // $('.story-nav ul').append(
      //   '<li><a href="#' + res.name + '">' + (res.title || res.name) + '</a></li>'
      // );

      if (typeof(res.mediatype) == 'undefined' || res.mediatype === null)
        res.mediatype = get_media_type(res.format);

      if (res.mediatype == 'application/vnd.datapackage+json') {
        pp = get_project_path(res.path);
        $.getJSON(pp, function(dp) {
          pp = pp.substring(0, pp.lastIndexOf('/')+1);
          load_DataPackage(dp, container, pp);
        });

      } else if (res.mediatype.indexOf('image/')==0) {
        rescount = rescount + 1;
        var item = add_gallery_item(container, rescount);
        if (item == null) return;

        var img = $('<img id="image-'+rescount+'" />').appendTo(item);
        imgpath = get_project_path(res.path, canonical_url);
        img.attr('style', 'background-image:url('+imgpath+')');

      } else if (res.mediatype == 'application/html') {
        rescount = rescount + 1;
        var item = add_gallery_item(container, rescount);
        if (item == null) return;

        imgpath = get_project_path(res.path, canonical_url);
        item.append('<iframe id="frame-'+rescount+'" src="' + imgpath + '"/>');

      } else if (res.mediatype == 'application/ipynb+json') {
        rescount = rescount + 1;
        var item = add_gallery_item(container, rescount);
        if (item == null) return;

        imgpath = get_project_path(res.path, canonical_url);
        imgpath = imgpath.replace('https://','').replace('http://','')
        nbpath = 'https://nbviewer.jupyter.org/urls/' + imgpath
        item.append('<iframe id="frame-'+rescount+'" src="' + nbpath + '"/>');

      } else if (res.mediatype == 'application/vnd.geo+json') {
        rescount = rescount + 1;
        var item = add_gallery_item(container, rescount);
        if (item == null) return;

        item.append('<div class="map" id="map-'+rescount+'" />');
        filepath = get_project_path(res.path, canonical_url);

        var lati = 47.38083877331195;
        var long = 8.548545854583836;
        var zoom = 9.28056836461962;

        var map = new mapboxgl.Map({
          container: 'map-' + rescount,
          style: 'mapbox://styles/mapbox/light-v9',
          zoom: zoom,
          center: { lat: lati, lng: long },
          trackResize: true
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

      container = false;
    }); // -each renderings

    // Enable fullscreen controls
    initFullScreen();

    /*
    // Pagination (currently not used)
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

  } //-load_DataPackage

  // Check compatibility
  if (get_ie_version() && get_ie_version() < 12) {
    $('<div class="alert alert-danger" role="alert">' +
      'Internet Explorer wird nicht vollständig unterstützt. Versuchen Sie es bitte erneut mit einem aktuellen Browser: ' +
      '<a href="http://outdatedbrowser.com/de" target="_blank">outdatedbrowser.com</a>' +
      '</div>').prependTo('.row:first');
  }

  // Load selected project
  if (typeof PROJECT_ID != 'undefined') {
    project_path = '/api/project/' + PROJECT_ID;
  } else if (typeof PROJECT_ROOT != 'undefined') {
    project_path = PROJECT_ROOT + '/datapackage.json';
  }
  if (project_path)
    $.getJSON(project_path, load_DataPackage);

  // setStoryLayout();
  // $(window).resize(setStoryLayout);

  if (typeof mapboxgl !== 'undefined')
    mapboxgl.accessToken = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA';

  if (typeof mermaid !== 'undefined')
    mermaid.initialize({startOnLoad:true});

    // Load the project menu
    /*
    $('rg-drawer').each(function() {
      var self = this;
      return; // Or don't..
      $.getJSON('/api/projects', function(projects) {
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
    */

    // Enable project-wide sharing button
    $('#embed-project').click(function() {
      var html = $(this).parents('.modal').find('.card-body').html();
      window.prompt('Copy this code to embed:', html.trim().replace(/  /g, ' '));
    });

});
