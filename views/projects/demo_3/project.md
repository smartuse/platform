---
title: Trends
template: templates/project.pug
name: "smartuse-political"
author: "HSA"
mapinfo: "Räumliche Trends in der Metropolitanregion"
categories:
 - bauland
 - politisch
 - wanderung
 - reserven
 - featured
"date-created": "2018-02-20"
updated: "Februar 2018"
resources:
 -
  name: "oev-edges"
  description: "ÖV S-Bahn Linien"
  author: ""
  link: ""
  path: "data/00-oev-edges.geojson"
  "spatial-profile": "simple-vector"
  type: line
  linewidth: 1
  color: "#000"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "oev-stations"
  description: "ÖV S-Bahn Haltestellen"
  author: ""
  link: ""
  path: "data/00-oev-stations.geojson"
  "spatial-profile": "simple-vector"
  type: filled-circle
  linewidth: 1
  color: "#000"
  fillcolor: "#000"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "gemeinde-stats"
  description: "Statistiken zu Politik, Bauland und Wanderung"
  author: "Statistik Amt Zürich"
  link: ""
  path: "data/3-00-GemeindeStats.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "political-shift-geojson"
  description: "Politische Verschiebung Kantonsratswahl Kanton Zürich"
  author: "Statistik Amt Zürich"
  link: ""
  path: "data/3-00-PoliticalShift.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: -7.4
    max: 3.2
    caption: "Verschiebung nach links bzw. rechts (in %)"
 -
  name: "political-shift"
  description: "Politische Verschiebung Kantonsratswahl Kanton Zürich"
  author: "Statistik Amt Zürich"
  link: ""
  path: "data/3-01-Politische-Verschiebung-KRW-2011-2015-links-rechts-gridded.tif"
  format: geotiff
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: -7.4
    max: 3.2
    caption: "Verschiebung nach links bzw. rechts (in %)"
 -
  name: "baulandreserve"
  description: "Baulandreserve"
  author: "Statistik Amt Zürich"
  link: ""
  path: "data/3-02-Baulandreserve-ha-gridded.tif"
  format: geotiff
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: 11
    max: 4427
    caption: "Baulandreserve in ha"
 -
  name: "wanderungssaldo"
  description: "Wanderungssaldo"
  author: "Statistik Amt Zürich"
  link: ""
  path: "data/3-03-Wanderungssaldo-gridded.tif"
  type: filled-polygon
  format: geotiff
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: -57
    max: 5857
    caption: "Wanderungssaldo (P./Jahr)"

compositions:
 -
  name: "01-political-shift"
  mapinfo: "Politische Verschiebung Kantonsratswahlen 2011 zu 2015"
  mapstyle: "simple-grey"
  layers:
   - political-shift-geojson
   - oev-edges
   - oev-stations
 -
  name: "02-baulandreserve"
  mapinfo: "Baulandreserven in ha"
  mapstyle: "simple-grey"
  layers:
   - gemeinde-stats:
    - layer:
     - gemeinde64
   - oev-edges
   - oev-stations
 -
  name: "03-wanderungssaldo"
  mapinfo: "Wanderungssaldo"
  mapstyle: "simple-grey"
  layers:
   - gemeinde-stats:
    - layer:
     - gemeinde99
   - oev-edges
   - oev-stations
 
---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.