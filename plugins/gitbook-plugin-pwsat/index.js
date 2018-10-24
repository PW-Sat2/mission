module.exports = {
    // Map of hooks
    hooks: {
    },

    // Map of new blocks
    blocks: {
        read_file: require('./read_file'),
        checklist: require('./checklist')
    },

    // Map of new filters
    filters: {
        page_folder: require('./page_folder')
    }
};