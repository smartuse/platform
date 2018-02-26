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

          var map = new mapboxgl.Map({
            container: 'map-' + ii,
            style: 'mapbox://styles/mapbox/light-v9',
            zoom: 9.28056836461962,
            center: { lat: 47.38083877331195, lng: 8.548545854583836 }
          });
          map.on('load', function () {
            map.addLayer({
              "id": "points",
              "type": "symbol",
              "source": {
                  "type": "geojson",
                  "data": geojson
              },
              "layout": {
                  "icon-image": "{icon}-15",
                  "text-field": "{title}",
                  "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                  "text-offset": [0, 0.6],
                  "text-anchor": "top"
              }
            });
          });

          maps[ii] = map;

        });
      }

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
