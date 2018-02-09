
/*!
 * Module dependencies.
 */

exports.index = function (req, res) {
  res.render('index');
};

exports.sample = function (req, res) {
  res.render('projects/sample_project/project');
};
