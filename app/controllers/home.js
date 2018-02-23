/*!
 * Home views
 */
const Package = require('datapackage');

exports.index = function (req, res) {
  res.render('index');
};

exports.sample = function (req, res) {
  // const dataPackage = Package.load('projects/sample_project/datapackage.json');
  // const resource = dataPackage.getResource('office-locations-geojson');
  // resource.read().then(function(data) { console.log(data); console.log('read'); });
  // console.log(resource);
  res.render('projects/sample_project/project');
};

exports.sample1 = function (req, res) {
  res.render('projects/project_1/project');
};
exports.sample2 = function (req, res) {
  res.render('projects/project_2/project');
};
exports.sample3 = function (req, res) {
  res.render('projects/project_3/project');
};
