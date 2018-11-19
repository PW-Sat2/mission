module.exports = {
    // Map of hooks
    hooks: {
    },

    // Map of new blocks
    blocks: {
        read_file: require('./read_file'),
        checklist: require('./checklist'),
        artifacts: require('./artifacts'),
        subpages:  require('./subpages')
    },

    // Map of new filters
    filters: {
        page_folder: require('./page_folder')
    }
};