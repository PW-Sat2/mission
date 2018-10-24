module.exports = {
    process: function(block) {
        const contentPath = block.args[0];
        const content = this.readFileAsString(contentPath);

        return content.then(c => ({
            body: `\`\`\`python\n${c}\n\`\`\``,
            parse: true
        }), c => ({
            body: `Missing file ${contentPath}`,
            parse: true
        }));
    }
};