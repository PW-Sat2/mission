module.exports = {
    // Map of hooks
    hooks: {
        init: function() {
        }
    },

    // Map of new blocks
    blocks: {
        read_file: require('./read_file'),
        checklist: require('./checklist'),
        artifacts: require('./artifacts'),
        gallery: require('./gallery'),
        session_templates:  require('./session_templates'),
        sessions: require('./sessions'),
        session_data: require('./session_data')
    },

    // Map of new filters
    filters: {
        page_folder: require('./page_folder')
    }
};
