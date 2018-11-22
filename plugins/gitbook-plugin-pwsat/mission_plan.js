const subpages = require('./subpages');
const fs = require('fs');

const UNDEFINED = "[TBD]";

const MISSION_PLAN_PATH = "mission_plan/progress.json";
const MISSION_PLAN_KEY = 'Mission Plan';

function extractPhaseId(phaseMarkdownLink){
    return phaseMarkdownLink.split("/").slice(-2)[0];
}

module.exports = {
    readMissionPlan: function() {
        const missionPlan = JSON.parse(fs.readFileSync(MISSION_PLAN_PATH))[MISSION_PLAN_KEY];
    
        const phaseMarkdownLinks = [];
        const phasesProgress = [];
        const phaseIds = [];
    
        for (let phase of Object.keys(missionPlan)) {
            phaseIds.push(extractPhaseId(phase));
            phaseMarkdownLinks.push(phase);
            phasesProgress.push(missionPlan[phase]);
        }
    
        return [phaseIds, phaseMarkdownLinks, phasesProgress];
    },

    getPhaseMarkdownLink: function(requestedPhaseId) {
        const phaseIds = module.exports.readMissionPlan()[0];

        for (let id = 0; id < phaseIds.length; id++) {
            if (requestedPhaseId === phaseIds[id]) {
                return module.exports.readMissionPlan()[1][id];
            }
        }

        return UNDEFINED;
    }
}
