const subpages = require('./subpages');
const session_data = require('./session_data');

const SESSIONS_PATH = "sessions";
const SESSIONS_IGNORED = ["index.md", "_templates", "_layout", "gallery.md"];

function buildGallery() {
    const items = subpages.getSubpages(SESSIONS_PATH);
        const items_filtered = subpages.filterItems(items, SESSIONS_IGNORED);
        const sessionPaths = subpages.buildSubpagesPaths(SESSIONS_PATH, items_filtered);
    
        var sessionPhotosLinks = [];
        for (let index = 0; index < sessionPaths.length; index++) {
            const dirName = (index + 1).toString();
            const sessionDir = SESSIONS_PATH + "/" + dirName + "/";
            const sessionPhotos = subpages.filterSessionPhotos(sessionDir);

            if (sessionPhotos.length > 0){
                const sessionMarkdownPhotos =  subpages.getPhotosMarkdownLinks(sessionDir, sessionPhotos);
                sessionPhotosLinks.push(sessionMarkdownPhotos);
                
                const sessionStartTime =  session_data.getStartTime(sessionDir);
                sessionPhotosLinks.push(`_${sessionStartTime}_\n`);
                sessionPhotosLinks.push(`## [Session ${index + 1}](${sessionDir})`);
            }
        }

        return sessionPhotosLinks.reverse();
}

module.exports = {
    process: function(block) {
        photos = buildGallery();
        photos = photos.join('\n');
        return {
            body: photos,
            parse: true
        }
    },
}
