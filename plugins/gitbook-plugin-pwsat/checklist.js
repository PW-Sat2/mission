const _ = require('lodash');
const CHECKED_MARK = "<span style='color:green;font-size:200%'>&#x2611;</span>";
const UNCHECKED_MARK = "<span style='color:red;font-size:200%'>&#x2610;</span>";

function readChecklist(ctx, path) {   
    return ctx.readFileAsString(path).then(c => JSON.parse(c), () => ({}));
}

function buildDisplayItem(name, value) {
    const checked = value[0] === true ? CHECKED_MARK : UNCHECKED_MARK;
    return `|${checked}|${name}|${value[1]}|`;
}

function buildDisplayStage(stageItems) {
    return Object.keys(stageItems)
        .map(name => buildDisplayItem(name, stageItems[name]));
}

function buildDisplayTop(checklist) {
    var result = [];
    for (let stage of Object.keys(checklist)) {
        result = [
            ...result,
            `### ${stage}`,
            `|**Status**|**Tasks**|`,
            '|:--------:|:-------|',
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
