---
title: Politische Veränderung
template: templates/project.pug
name: "smartuse-political"
author: "HSA"
mapinfo: "Geschossflächenreserven in der Metropolitanregion, separiert nach Zonenzugehörigkeit (Wohnen, Industrie und Mischzonen)"
categories:
 - geschossflaechen
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
  name: "geschossflaechen-reserve-industrie"
  description: "Geschossflaechenreserven Industriezonen"
  author: "Amtliche Vermessung Kanton Zürich"
  link: ""
  path: "data/01-geschossflaechen-industrie.geojson"
  "spatial-profile": "simple-vector"
  type: filled-polygon
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
-
  name: "geschossflaechen-reserve-misch"
  description: "Geschossflaechenreserven Mischzonen"
  author: "Amtliche Vermessung Kanton Zürich"
  link: ""
  path: "data/01-geschossflaechen-misch.geojson"
  "spatial-profile": "simple-vector"
  type: filled-polygon
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
-
  name: "geschossflaechen-reserve-wohnen"
  description: "Geschossflaechenreserven Wohnzonen"
  author: "Amtliche Vermessung Kanton Zürich"
  link: ""
  path: "data/01-geschossflaechen-wohnen.geojson"
  "spatial-profile": "simple-vector"
  type: filled-polygon
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
-
  name: "geschossflaechen-reserve"
  description: "Geschossflaechenreserven"
  author: "Amtliche Vermessung Kanton Zürich"
  link: ""
  path: "data/01-geschossflaechen-reserve.geojson"
  "spatial-profile": "simple-vector"
  type: filled-polygon
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
-
  name: "density-people"
  description: "Personendichte"
  author: "Copernicus Land Use, Urban Atlas"
  link: ""
  path: "data/02-personendichte.geojson"
  "spatial-profile": "simple-vector"
  type: filled-polygon
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
compositions:
 -
  name: "Geschossflächenreserven Industrie"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Industriezonen"
  mapstyle: "simple-grey"
  layers:
   - geschossflaechen-reserve-industrie
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven Mischzonen"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Mischzonen"
  mapstyle: "simple-grey"
  layers:
   - geschossflaechen-reserve-wohnen
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven Wohnen"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Wohnzonen"
  mapstyle: "simple-grey"
  layers:
   - geschossflaechen-reserve-wohnen
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion nach Zonenzugehörigkeit"
  mapstyle: "simple-grey"
  layers:
   - geschossflaechen-reserve-kombiniert
   - oev-edges
   - oev-stations
 -
  name: "Personendichte"
  mapinfo: "Personendichte in der Metropolitanregion"
  mapstyle: "simple-grey"
  layers:
   - density-people
   - oev-edges
   - oev-stations
---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.