---
title: Sample project
template: templates/project.pug
name: "smartuse-sample"
author: "Grün Stadt Zürich, Tiefbau- und Entsorgungsdepartement"
updated: "April 2018"
categories:
 - trees
 - government
 - featured
---

This is a sample model shared in the SmartUse application. Projects are managed in the database, and any files they provide stored in this folder. This may include:

- Markdown content such as this text
- Point data (CSV, GeoJSON)
- Vector data (GeoJSON, GeoPackage, Shapefile)
- Pixel data (PNG, JPEG, TIFF, GeoTIFF)

The project metadata itself is specified in a JSON structure, currently in a sample `datapackage.json` file in this folder, and later accessible through an API. The schema will be developed in accordance to the [Spatial Data Package](https://research.okfn.org/spatial-data-package-investigation/#point-datasets) standard.

The below map is rendered using [mapbox-gl-js](https://www.mapbox.com/mapbox-gl-js/).
We are planning to use the [Riot.js](http://riotjs.com/) library to build out the frontend.
