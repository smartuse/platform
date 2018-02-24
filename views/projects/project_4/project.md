---
title: Die funktionale Region
template: templates/project.pug
name: "smartuse-swisscom"
author: "Swisscom"
mapinfo: "Nutzung um den HB Zürich"
categories:
 - nutzung
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
  name: "day-program-passive"
  description: "Nutzungen Tag"
  author: "OpenStreetMap Contributors"
  link: "https://www.openstreemap.org"
  path: "data/00-day-program.geojson"
  "spatial-profile": "simple-vector"
  type: filled-circle
  linewidth: 1
  color: "#ccc"
  fillcolor: "#ccc"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "day-program-active"
  description: "Nutzungen Tag"
  author: "OpenStreetMap Contributors"
  link: "https://www.openstreemap.org"
  path: "data/00-day-program.geojson"
  "spatial-profile": "simple-vector"
  type: filled-circle
  linewidth: 1
  color: "#fff51e"
  fillcolor: "#fff51e"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "night-program-passive"
  description: "Nutzungen Nacht"
  author: "OpenStreetMap Contributors"
  link: "https://www.openstreemap.org"
  path: "data/00-night-program.geojson"
  "spatial-profile": "simple-vector"
  type: filled-circle
  linewidth: 1
  color: "#ccc"
  fillcolor: "#ccc"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "night-program-active"
  description: "Nutzungen Nacht"
  author: "OpenStreetMap Contributors"
  link: "https://www.openstreemap.org"
  path: "data/00-night-program.geojson"
  "spatial-profile": "simple-vector"
  type: filled-circle
  linewidth: 1
  color: "#fff51e"
  fillcolor: "#fff51e"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
 -
  name: "swisscom-hb-03-04"
  description: "Heatmap HB 03.00-04.00"
  author: "Swisscom"
  link: ""
  path: "data/01-heatmaps-zurich-central-station-29022016-03000400.geojson"
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
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
 -
  name: "swisscom-hb-08-09"
  description: "Heatmap HB 08.00-09.00"
  author: "Swisscom"
  link: ""
  path: "data/02-heatmaps-zurich-central-station-29022016-08000900.geojson"
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
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
 -
  name: "swisscom-hb-16-17"
  description: "Heatmap HB 16.00-17.00"
  author: "Swisscom"
  link: ""
  path: "data/03-heatmaps-zurich-central-station-29022016-16001700.geojson"
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
    min: 0
    max: 2646
    caption: "Geschossflächenreserven in 1000 m2"
compositions:
 -
  name: "nutzung-0809"
  mapinfo: "Nutzung morgens, 08:00-09:00"
  mapstyle: "simple-grey"
  layers:
   - swisscom-hb-08-09
   - oev-edges
   - oev-stations
   - day-program-active
   - night-program-passive
 -
  name: "nutzung-1617"
  mapinfo: "Nutzung morgens, 16:00-17:00"
  mapstyle: "simple-grey"
  layers:
   - swisscom-hb-16-17
   - oev-edges
   - oev-stations
   - day-program-active
   - night-program-passive
 -
  name: "nutzung-0304"
  mapinfo: "Nutzung morgens, 03:00-04:00"
  mapstyle: "simple-grey"
  layers:
   - swisscom-hb-03-04
   - oev-edges
   - oev-stations
   - day-program-passive
   - night-program-active
---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.