---
title: Elastisch und Mobil
summary: "Geschossflächenreserven in der Metropolitanregion, separiert nach Zonenzugehörigkeit (Wohnen, Industrie und Mischzonen)"
template: templates/project.pug
author: "HSA"
categories:
 - geschossflaechen
 - reserven
 - featured
updated: "Februar 2018"
compositions:
 -
  name: "Geschossflächenreserven Industrie"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Industriezonen"
  mapstyle: "light-v9"
  layers:
   - geschossflaechen-reserve-industrie
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven Mischzonen"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Mischzonen"
  mapstyle: "light-v9"
  layers:
   - geschossflaechen-reserve-wohnen
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven Wohnen"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion Wohnzonen"
  mapstyle: "light-v9"
  layers:
   - geschossflaechen-reserve-wohnen
   - oev-edges
   - oev-stations
 -
  name: "Geschossflächenreserven"
  mapinfo: "Geschossflächenreserven in der Metropolitanregion nach Zonenzugehörigkeit"
  mapstyle: "light-v9"
  layers:
   - geschossflaechen-reserve-kombiniert
   - oev-edges
   - oev-stations
 -
  name: "Personendichte"
  mapinfo: "Personendichte in der Metropolitanregion"
  mapstyle: "light-v9"
  layers:
   - density-people
   - oev-edges
   - oev-stations
---

Die Metropolitanregion Zürich besteht aus einer vielzahl an Gemeinden, die in ihrer Unterschiedlichkeit die Region ausmachen. Diese Zusammenstellung verdeutlicht die Abhängkeiten zwischen tatsächlich gebautem Raum, planerischer Intention und realer Nutzung.
