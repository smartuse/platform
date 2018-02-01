var map;

Zepto(function($){

  riot.mount('sample');

  mapboxgl.accessToken = 'pk.eyJ1Ijoic21hcnR1c2UiLCJhIjoiY2pkNGowcGdzMHhpbzMzcWp3eGYydGhmMiJ9.k9QyYo-2pFvyyFDJiz16UA';
  map = new mapboxgl.Map({
    container: 'testmap',
    style: 'mapbox://styles/mapbox/streets-v10',
    zoom: 9.28056836461962,
    center: { lng: 8.548545854583836, lat: 47.38083877331195 }
  });


});
