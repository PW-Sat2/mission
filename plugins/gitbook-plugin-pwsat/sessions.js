const subpages = require('./subpages');

function buildSessions(pathToRead, items_filtered) {
    markdownLinks = subpages.buildMarkdownLinks(pathToRead, items_filtered);
    pagesPaths = subpages.buildSubpagesLinks(pathToRead, items_filtered);

    sessions = [];
    for (let index = 0; index < markdownLinks.length; index++) {
        const singleLink = markdownLinks[index];
        sessions.push(`|${singleLink}|MISSING|MISSING|MISSING|MISSING|`);
    }
    return sessions;
}

function buildTable(pathToRead, items_filtered) {
    var result = [];
    result = [
        ...result,
        `|**Index**|**Time**|**Phase**|**Status**|**Short description**|`,
        `|-|-|-|-|-|`,
        ...buildSessions(pathToRead, items_filtered),
        ''
    ];
    return result;
}

module.exports = {
    process: function(block) {
        const pathToRead = "sessions";
        const ignoredItems = ["index.md", "_templates", "_layout"];

        const ctx = this;
        const items = subpages.getSubpages(ctx.resolve(pathToRead));

        items_filtered = subpages.filterItems(items, ignoredItems);

        const links = [
            ...buildTable(pathToRead, items_filtered)
        ];

        return {
            body: links.join('\n'),
            parse: true
        }
    }
}
