---
title: Sample project
template: templates/project.pug
name: "smartuse-sample"
author: "Grün Stadt Zürich, Tiefbau- und Entsorgungsdepartement"
mapinfo: "Donec ut ullamcorper nisl, quis auctor velit. Mauris sit amet posuere metus. Nulla urna purus, finibus et arcu venenatis, semper lacinia diam. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Sed et ante ante. Integer blandit, ipsum blandit dignissim scelerisque, ex sapien pulvinar diam, quis facilisis dolor justo in dui."
categories:
 - trees
 - government
 - featured
"date-created": "2018-01-01"
updated: "April 2018"
resources:
 -
  name: "treedensity-zurich"
  description: "A sample dataset courtesy of Thorben"
  path: "data/TreeDensity-Zurich.geojson"
  "spatial-profile": "simple-vector"
  format: geojson
  view:
   lat: 0.5
   lon: 42.1
   zoom: 19.1
  legend:
   -
    type: range
    min: 0
    max: 255
    caption: "The range of tree sizes, measured in cm"
 -
  name: "office-locations-geojson"
  description: "Sample data in GeoJSON format"
  path: "data/lat-lon.geojson"
  "spatial-profile": "simple-vector"
  format: geojson
---

This is a sample model shared in the SmartUse application. Projects are managed in the database, and any files they provide stored in this folder. This may include:

- Markdown content such as this text
- Point data (CSV, GeoJSON)
- Vector data (GeoJSON, GeoPackage, Shapefile)
- Pixel data (PNG, JPEG, TIFF, GeoTIFF)

The project metadata itself is specified in a JSON structure, currently in a sample `datapackage.json` file in this folder, and later accessible through an API. The schema will be developed in accordance to the [Spatial Data Package](https://research.okfn.org/spatial-data-package-investigation/#point-datasets) standard.

The below map is rendered using [mapbox-gl-js](https://www.mapbox.com/mapbox-gl-js/).
We are planning to use the [Riot.js](http://riotjs.com/) library to build out the frontend.
