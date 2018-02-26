var maps = {};

Zepto(function($){

  $.getJSON('/' + project_path + '/datapackage.json', function(datapackage) {
    gallery = $('.gallery'); //.html('<div class="controls"></div>');
    var rescount = datapackage.resources.length;
    gallery.addClass('items-' + rescount);
    // console.log(datapackage);
    $.each(datapackage.resources, function(i, res) {
      var ii = i + 1;
      gallery.append('<div id="item-'+ii+'" class="control-operator"></div>');
      // gallery.find('.controls').append('<a href="#item-'+ii+'" class="control-button">•</a>');
      item = gallery.append('<figure class="item" />').find('.item:last-child');

      if (res.format == 'image') {
        img = item.append('<img id="image-'+ii+'" />').find('img:last-child');
        imgpath = '/' + project_path + '/' + res.path;
        img.attr('style', 'background-image:url('+imgpath+')');

      } else if (res.format == 'geojson') {
        item.append('<div class="map" id="map-'+ii+'" />');
        filepath = (res.path.indexOf('http')<0) ?
          '/' + project_path + '/' + res.path : res.path;
        $.getJSON(filepath, function(geojson) {

          var lati = 47.38083877331195;
          var long = 8.548545854583836;
          var zoom = 9.28056836461962;

          var map = new mapboxgl.Map({
            container: 'map-' + ii,
            style: 'mapbox://styles/mapbox/light-v9',
            zoom: zoom,
            center: { lat: lati, lng: long }
          });

          var layer = {
            "id": res.name,
            "type": res.type || "symbol"
          };

          if (res.type == "line")
            layer["paint"] = {
                "line-color": res.color || "#888",
                "line-width": res.linewidth || 3
            };

          if (res.type == "circle")
            layer["paint"] = {
                "circle-color": res.fillcolor || "#000",
                "circle-radius": res.fillradius || 2,
            };

          if (res.type == "fill")
            layer["paint"] = {
                "fill-color": res.fillcolor || "#088",
                "fill-opacity": res.fillopacity || 0.8,
            };

          if (res.type == "symbol")
            layer["layout"] = {
                "icon-image": "{icon}-15",
                "text-field": "{title}",
                "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                "text-offset": [0, 0.6],
                "text-anchor": "top"
            };

          layer["source"] = {
              "type": "geojson",
              "data": geojson
          };

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

          maps[ii] = map;

        });
      }

      if (res.name.length>1 && res.description.length>1)
        item.append('<div class="description">'
        + '<small>' + res.name + '</small><br>'
        + res.description + '</div>')
    });

    var tags = riot.mount('rg-pagination', {
      pagination: {
        pages: rescount,
        page: 1
      }
    });
    tags[0].on('page', function (page) {
      location.href="#item-" + page;
      if (maps.hasOwnProperty(page))
        maps[page].resize();
    });
    location.href="#item-1";

  });
// .basemap#testmap

  // riot.mount('sample');

  mapboxgl.accessToken = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA';

});
