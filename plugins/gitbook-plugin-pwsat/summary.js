const fs = require('fs');
const subpages = require('./subpages');
const session_data = require('./session_data');
const sessions = require('./sessions');
const mission_plan = require('./mission_plan');

const SUMMARY_PATH = "SUMMARY.md";
const SESSION_TEMPLATES_PATH = 'sessions/_templates'
const SESSION_TEMPLATES_IGNORED = ['index.md']

function missionPlanGenerator() {
    const missionPlan = mission_plan.readMissionPlan();
    var outputMarkdownLinks = []

    for (let phase = 0; phase < missionPlan[1].length; phase++) {
        outputMarkdownLinks.push('    * ' + missionPlan[1][phase]);
    }

    return outputMarkdownLinks;
}

function templatesMarkdownLinks() {
    const items = subpages.getSubpages(SESSION_TEMPLATES_PATH);
    const items_filtered = subpages.filterItems(items, SESSION_TEMPLATES_IGNORED);
    const markdownLinks = subpages.buildMarkdownLinks(SESSION_TEMPLATES_PATH, items_filtered)

    markdownLinksFormatted = []
    for (let item = 0; item < markdownLinks.length; item++) {
        markdownLinksFormatted.push('       * ' + markdownLinks[item]);
    }

    return markdownLinksFormatted;
}

function generate() {
    summary = [
        '* [Start](/README.md)',
        '* [Gallery](/gallery.md)',
        '* [Mission plan](/mission_plan/index.md)',
        ...missionPlanGenerator(),
        '* [Sessions](/sessions/index.md)',
        ...sessions.markdownLinks(),
        '    * [Templates](/sessions/_templates/index.md)',
        ...templatesMarkdownLinks()
    ]

    fs.writeFileSync(SUMMARY_PATH, summary.join('\n'));
}


console.info("Info: generating SUMMARY.md");
generate();
