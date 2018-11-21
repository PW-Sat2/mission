const subpages = require('./subpages');
const session_data = require('./session_data');

function buildSessions(resolvedPathToSessions, items_filtered) {
    markdownLinks = subpages.buildMarkdownLinks(resolvedPathToSessions, items_filtered);
    sessionPaths = subpages.buildSubpagesPaths(resolvedPathToSessions, items_filtered);

    sessions = [];
    for (let index = 0; index < markdownLinks.length; index++) {
        const sessionDir = resolvedPathToSessions + "\\" + (index + 1).toString() + "\\";

        const sessionStartTime =  session_data.getStartTime(sessionDir);
        const sessionPhase = session_data.getPhase(sessionDir);
        const sessionStatus = session_data.getStatus(sessionDir);
        const sessionDescription = session_data.getShortDescription(sessionDir);

        sessions.push(`|${markdownLinks[index]}|${sessionStartTime}|${sessionPhase}|${sessionStatus}|${sessionDescription}|`);
    }
    return sessions.reverse();
}

function buildTable(resolvedPathToSessions, items_filtered) {
    var result = [];
    result = [
        ...result,
        `|**Index**|**Start Time**|**Phase**|**Status**|**Short description**|`,
        `|:-:|:-:|:-:|:-:|:-|`,
        ...buildSessions(resolvedPathToSessions, items_filtered),
        ''
    ];
    return result;
}

module.exports = {
    process: function(block) {
        const pathToSessions = "sessions";
        const ignoredItems = ["index.md", "_templates", "_layout"];

        const ctx = this;
        const items = subpages.getSubpages(ctx.resolve(pathToSessions));

        items_filtered = subpages.filterItems(items, ignoredItems);

        const links = [
            ...buildTable(ctx.resolve(pathToSessions), items_filtered)
        ];

        return {
            body: links.join('\n'),
            parse: true
        }
    }
}
