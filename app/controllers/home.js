/*!
 * Home views
 */

exports.index = function (req, res) {
  res.render('index');
};

exports.project = function (req, res) {
  ppath = 'projects/' + req.params.uid;
  res.render(ppath + '/project', {
    path: ppath
  });
};
