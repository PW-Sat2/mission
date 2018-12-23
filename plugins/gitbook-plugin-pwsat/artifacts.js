const fs = require('fs');
const _ = require('lodash');
const path = require('path');

String.prototype.contains = function(test) {
    return this.indexOf(test) == -1 ? false : true;
};

function getArtifacts(folder) {
    if (!fs.existsSync(folder)) {
        return [];
    }

    items = fs.readdirSync(folder)
        .filter(f => f != '.keep')
        .filter(f => f != 'assembled')
        .filter(f => !f.contains("uplink"))
        ;

    let assembled = [];

    if (fs.existsSync(path.join(folder, 'assembled'))) {
        assembled = fs.readdirSync(path.join(folder, 'assembled'))
                .map(f => path.join('assembled', f));
    }

    return items.concat(assembled);
}

function missingList(items) {
    return items.map(i => `* MISSING: ${i}`);
}

function foundList(items) {
    return items.map(i => `* <a href="artifacts/${i}" target="_blank">${i}<a/>`);
}

module.exports = {
    process: function(block) {
        const ctx = this;

        const artifactsFolder = ctx.resolve(block.args[0]);
        const requiredArtifacts = block.args[1];

        const artifacts = getArtifacts(artifactsFolder);

        const missingRequired = _.difference(requiredArtifacts, artifacts);        

        const items = [
            ...missingList(missingRequired),
            ...foundList(artifacts)
        ];

        return {
            body: items.join('\n'),
            parse: true
        }
    }
}