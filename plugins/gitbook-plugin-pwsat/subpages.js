const fs = require('fs');

function isItemIgnored(item, ignoredItems) {
    for (let index = 0; index < ignoredItems.length; index++) {
        if (ignoredItems[index] === item) {
            return true;
        }
    }
    return false;
}

module.exports = {
    getSubpages: function(ResolvedPathToRead) {
        if (!fs.existsSync(ResolvedPathToRead)) {
            return [];
        }
        return fs.readdirSync(ResolvedPathToRead);
    },

    buildSubpagesLinks: function(pathToRead, items) {
        return items.map(i => `/${pathToRead}/${i}/index.md`);
    },

    buildMarkdownLinks: function(pathToRead, items) {
        return items.map(i => `[${i}](/${pathToRead}/${i}/index.md)`);
    },

    filterItems: function(items, itemsToFilter) {
        var items_filtered = []
        for (let index = 0; index < items.length; index++) {
            const item = items[index];
            if (!isItemIgnored(item, itemsToFilter)) {
                items_filtered.push(item);
            }
        }
        return items_filtered;
    }
};
