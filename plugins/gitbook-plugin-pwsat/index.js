const fs = require('fs');
const path = require('path');

module.exports = {
    // Map of hooks
    hooks: {
    },

    // Map of new blocks
    blocks: {
        read_file: {
            process: function(block) {
                const contentPath = block.args[0];
                const content = this.readFileAsString(contentPath);
    
                return content.then(c => ({
                    body: `\`\`\`python\n${c}\n\`\`\``,
                    parse: true
                }), c => ({
                    body: 'Missing block',
                    parse: true
                }));
            }
        }
    },

    // Map of new filters
    filters: {
        page_folder: function(p) {
            return path.basename(path.dirname(p));
        }
    }
};