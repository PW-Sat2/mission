const fs = require('fs');
const _ = require('lodash');

function getArtifacts(folder) {
    if (!fs.existsSync(folder)) {
        return [];
    }

    return fs.readdirSync(folder);
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