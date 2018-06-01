---
title: Trends
summary: "Räumliche Trends in der Metropolitanregion"
template: templates/project.pug
author: "HSA"
categories:
 - bauland
 - politisch
 - wanderung
 - reserven
 - featured
updated: "Februar 2018"
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
   - gemeinde-stats: gemeinde64
   - oev-edges
   - oev-stations
 -
  name: "03-wanderungssaldo"
  mapinfo: "Wanderungssaldo"
  mapstyle: "simple-grey"
  layers:
   - gemeinde-stats: gemeinde99
   - oev-edges
   - oev-stations

---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.
