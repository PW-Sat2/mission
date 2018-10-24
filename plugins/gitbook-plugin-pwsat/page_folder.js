const path = require('path');

module.exports = function(p) {
    return path.basename(path.dirname(p));
}