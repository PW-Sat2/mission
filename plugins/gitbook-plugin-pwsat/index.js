module.exports = {
    // Map of hooks
    hooks: {
    },

    // Map of new blocks
    blocks: {
        read_file: require('./read_file'),
        checklist: require('./checklist'),
        artifacts: require('./artifacts'),
        session_templates:  require('./session_templates'),
        sessions: require('./sessions')
    },

    // Map of new filters
    filters: {
        page_folder: require('./page_folder')
    }
};