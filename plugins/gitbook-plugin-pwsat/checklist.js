const _ = require('lodash');

function readChecklist(ctx, path) {   
    return ctx.readFileAsString(path).then(c => JSON.parse(c), () => ({}));
}

function buildDisplayItem(name, value) {
    const checked = value === true ? "checked" : "";
    return `<input type="checkbox" disabled ${checked}> ${name}`;
}

function buildDisplayStage(stageItems) {
    return Object.keys(stageItems)
        .sort()
        .map(name => buildDisplayItem(name, stageItems[name]));
}

function buildDisplayTop(checklist) {
    var result = [];
    for (let stage of Object.keys(checklist)) {
        result = [
            ...result,
            `### ${stage}`,
            '',
            ...buildDisplayStage(checklist[stage]),
            ''
        ];        
    }

    return result;
}

module.exports = {
    process: function(block) {
        var ctx = this;
        
        return Promise.all([
            readChecklist(ctx, block.args[0]),
            readChecklist(ctx, block.args[1]),
        ])
        .then(parts => _.merge({}, ...parts))
        .then(checklist => buildDisplayTop(checklist))
        .then(text => ({
            body: text.join('\n'),
            parse: true
        }));
    }
};