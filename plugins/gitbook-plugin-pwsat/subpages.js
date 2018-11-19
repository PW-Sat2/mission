const fs = require('fs');
const _ = require('lodash');

function getArtifacts(folder) {
    if (!fs.existsSync(folder)) {
        return [];
    }

    return fs.readdirSync(folder);
}

function foundList(pathToRead, items) {
    //return items.map(i => `* <a href="${pathToRead}/${i}/index.md" target="_blank">${i}<a/>`);
    return items.map(i => `* [${i}](/${pathToRead}/${i}/index.md)`);
}

module.exports = {
    process: function(block) {
        const ctx = this;

        const pathToRead = ctx.resolve(block.args[0]);
        const folders = getArtifacts(pathToRead);

        const items = [
            ...foundList(block.args[0], folders)
        ];

        return {
            body: items.join('\n'),
            parse: true
        }
    }
}
