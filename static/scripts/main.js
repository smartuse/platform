var map;

Zepto(function($){

  riot.mount('sample');

  var tags = riot.mount('rg-pagination', {
    pagination: {
      pages: 10,
      page: 6
    }
  });

  tags[0].on('page', function (page) { console.log(page) });

  mapboxgl.accessToken = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA';
  map = new mapboxgl.Map({
    container: 'testmap',
    style: 'mapbox://styles/mapbox/streets-v10',
    zoom: 9.28056836461962,
    center: { lat: 47.38083877331195, lng: 8.548545854583836 }
  });

  geojson = {"type":"FeatureCollection","features":[{"type":"Feature","geometry":{"type":"Point","coordinates":[8.3710467,47.4283927]},"properties":{"icon": "monument", "title":"Hosoya Schaefer"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[8.5039705,47.4085954]},"properties":{"icon": "monument", "title":"ETH Hönggenberg"}},{"type":"Feature","geometry":{"type":"Point","coordinates":[8.5315573,47.384887]},"properties":{"icon": "monument", "title":"Impact Hub Zürich - Colab"}}]};

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

});
