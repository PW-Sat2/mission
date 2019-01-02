const fs = require('fs');
const path = require('path');

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

    buildIndexLinks: function(pathToRead, items) {
        return items.map(i => `/${pathToRead}/${i}/index.md`);
    },

    buildSubpagesPaths: function(pathToRead, items) {
        return items.map(i => `/${pathToRead}/${i}/`);
    },

    buildItems: function(pathToRead, items) {
        return items.map(i => `${i}`);
    },

    buildMarkdownLinks: function(pathToRead, items) {
        return items.map(i => `[${i}](/${pathToRead}/${i}/index.md)`);
    },

    getPhotosMarkdownLinks: function(sessionDir, items){
        return items.map(i => `![Image](${sessionDir}/artifacts/${i})`);
    },

    filterSessionPhotos: function(sessionDir){
        let images = [];
        let files = fs.readdirSync(sessionDir + "/artifacts/");
        for (var i = 0, len = files.length; i < len; i++) {
            if(path.extname(files[i]) === ".jpg") {
                images.push(files[i]);
            }
        }
        return images;
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
