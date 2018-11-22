const subpages = require('./subpages');

module.exports = {
    process: function(block) {
        const pathToRead = "sessions/_templates";
        const ignoredItems = ["index.md"];

        const ctx = this;
        var items = subpages.getSubpages(ctx.resolve(pathToRead));

        items_filtered = subpages.filterItems(items, ignoredItems);

        const links = [
            ...subpages.buildMarkdownLinks(pathToRead, items_filtered)
        ];

        for (let index = 0; index <links.length; index++) {
            links[index] = '* ' + links[index]
        }

        return {
            body: links.join('\n'),
            parse: true
        }
    }
}
