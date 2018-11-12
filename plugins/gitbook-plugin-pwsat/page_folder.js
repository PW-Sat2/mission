const path = require('path');

module.exports = function(p) {
    return p.substring(0, p.lastIndexOf("/") + 1);
}