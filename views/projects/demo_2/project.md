---
title: Mobilitätsprofile
template: templates/project.pug
name: "smartuse-mobility"
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
-
  name: "01-pendlerorte"
  description: "Pendlerorte"
  author: "Amtliche Vermessung Kanton Zürich"
  link: ""
  path: "data/01-pendlerorte.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0.5
    max: 5.8
    caption: "Bew. pro Beschäft."
-
  name: "02-fischenthal-outline"
  description: "Fischenthal Outline"
  author: "Amt für Raumentwicklung "
  link: "http://www.geolion.zh.ch/geodatensatz/865"
  path: "data/02-fischenthal-miv.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "02-fischenthal-miv"
  description: "Fischenthal MIV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/02-fischenthal-miv.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 440
    caption: "Ø Personenwege pro Werktag"
-
  name: "02-fischenthal-miv-cluster"
  description: "Fischenthal MIV Cluster"
  author: "HSA "
  link: ""
  path: "data/02-fischenthal-miv-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "02-fischenthal-oev"
  description: "Fischenthal ÖV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/02-fischenthal-oev.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 55
    caption: "Ø Personenwege pro Werktag"
-
  name: "02-fischenthal-oev-cluster"
  description: "Fischenthal ÖV Cluster"
  author: "HSA "
  link: ""
  path: "data/02-fischenthal-oev-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "03-fehrenaltdorf-outline"
  description: "Fehrenaltdorf Outline"
  author: "Amt für Raumentwicklung "
  link: "http://www.geolion.zh.ch/geodatensatz/865"
  path: "data/03-fehrenaltdorf-miv.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "03-fehrenaltdorf-miv"
  description: "Fehrenaltdorf MIV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/03-fehrenaltdorf-miv.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 440
    caption: "Ø Personenwege pro Werktag"
-
  name: "03-fehrenaltdorf-miv-cluster"
  description: "Fehrenaltdorf MIV Cluster"
  author: "HSA "
  link: ""
  path: "data/03-fehrenaltdorf-miv-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "03-fehrenaltdorf-oev"
  description: "Fehrenaltdorf ÖV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/03-fehrenaltdorf-oev.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 55
    caption: "Ø Personenwege pro Werktag"
-
  name: "03-fehrenaltdorf-oev-cluster"
  description: "Fehrenaltdorf ÖV Cluster"
  author: "HSA "
  link: ""
  path: "data/03-fehrenaltdorf-oev-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "04-lufingen-outline"
  description: "Lufingen Outline"
  author: "Amt für Raumentwicklung "
  link: "http://www.geolion.zh.ch/geodatensatz/865"
  path: "data/04-lufingen-outline.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "04-lufingen-miv"
  description: "Lufingen MIV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/04-lufingen-miv.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 440
    caption: "Ø Personenwege pro Werktag"
-
  name: "04-lufingen-miv-cluster"
  description: "Lufingen MIV Cluster"
  author: "HSA "
  link: ""
  path: "data/04-lufingen-miv-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "04-lufingen-oev"
  description: "Lufingen ÖV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/04-lufingen-oev.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 55
    caption: "Ø Personenwege pro Werktag"
-
  name: "04-lufingen-oev-cluster"
  description: "Lufingen ÖV Cluster"
  author: "HSA "
  link: ""
  path: "data/04-lufingen-oev-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "05-neerach-outline"
  description: "Neerach Outline"
  author: "Amt für Raumentwicklung "
  link: "http://www.geolion.zh.ch/geodatensatz/865"
  path: "data/05-neerach-outline.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "05-neerach-miv"
  description: "Neerach MIV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/05-neerach-miv.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 440
    caption: "Ø Personenwege pro Werktag"
-
  name: "05-neerach-miv-cluster"
  description: "Neerach MIV Cluster"
  author: "HSA "
  link: ""
  path: "data/05-neerach-miv-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
-
  name: "05-neerach-oev"
  description: "Neerach ÖV Einzug"
  author: "Verkehrsamt Kanton Zürich"
  link: "https://afv.zh.ch/internet/volkswirtschaftsdirektion/afv/de/verkehrsgrundlagen/verkehrsnachfrage/verkehrsnachfrage_gemeinden.html"
  path: "data/05-neerach-oev.geojson"
  "spatial-profile": "simple-vector"
  type: filled-square
  format: geojson
  legend:
   -
    type: range
    min: 0
    max: 55
    caption: "Ø Personenwege pro Werktag"
-
  name: "05-neerach-oev-cluster"
  description: "Neerach ÖV Cluster"
  author: "HSA "
  link: ""
  path: "data/05-neerach-oev-cluster.geojson"
  "spatial-profile": "simple-vector"
  type: line
  format: geojson
compositions:
 -
  name: "Pendlerorte"
  mapinfo: "Einwohner pro Beschäftigem/r"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 01-pendlerorte
   - oev-edges
   - oev-stations
 -
  name: "Fischenthal-MIV"
  mapinfo: "Mobilitätsprofil MIV Fischenthal"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 02-fischenthal-miv
   - 02-fischenthal-miv-cluster
   - 02-fischenthal-outline
 -
  name: "Fischenthal-OEV"
  mapinfo: "Mobilitätsprofil ÖV Fischenthal"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 02-fischenthal-oev
   - 02-fischenthal-oev-cluster
   - 02-fischenthal-outline
   - oev-edges
   - oev-stations
 -
  name: "Fehrenaltdorf-MIV"
  mapinfo: "Mobilitätsprofil MIV Fehrenaltdorf"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 03-fehrenaltdorf-miv
   - 03-fehrenaltdorf-miv-cluster
   - 03-fehrenaltdorf-outline
 -
  name: "Fehrenaltdorf-OEV"
  mapinfo: "Mobilitätsprofil ÖV Fehrenaltdorf"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 03-fehrenaltdorf-oev
   - 03-fehrenaltdorf-oev-cluster
   - 03-fehrenaltdorf-outline
   - oev-edges
   - oev-stations
 -
  name: "Lufingen-MIV"
  mapinfo: "Mobilitätsprofil MIV Lufingen"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 04-lufingen-miv
   - 04-lufingen-miv-cluster
   - 04-lufingen-outline
 -
  name: "Lufingen-OEV"
  mapinfo: "Mobilitätsprofil ÖV Lufingen"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 04-lufingen-oev
   - 04-lufingen-oev-cluster
   - 04-lufingen-outline
   - oev-edges
   - oev-stations
 -
  name: "Neerach-MIV"
  mapinfo: "Mobilitätsprofil MIV Neerach"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 05-neerach-miv
   - 05-neerach-miv-cluster
   - 05-neerach-outline
 -
  name: "Neerach-OEV"
  mapinfo: "Mobilitätsprofil ÖV Neerach"
  mapstyle: "light-v9"
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  layers:
   - 05-neerach-oev
   - 05-neerach-oev-cluster
   - 05-neerach-outline
   - oev-edges
   - oev-stations
---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.