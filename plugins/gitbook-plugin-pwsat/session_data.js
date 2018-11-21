const fs = require('fs');
const mission_plan = require('./mission_plan');

const UNDEFINED = "[TBD]";

const STATUS_PLANNED = "planned";
const STATUS_FAILED = "failed";
const STATUS_SUCCESS = "success";

const STATUS_PLANNED_SYM = "<span style='color:orange;font-size:200%' title='Planned'>&#x231A;</span>";
const STATUS_FAILED_SYM = "<span style='color:red;font-size:200%' title='Failed'>&#x2612;</span>";
const STATUS_SUCCESS_SYM = "<span style='color:green;font-size:200%' title='Success'>&#x2611;</span>";


function readSessionData(resolvedPathToSessionData) {
    return JSON.parse(fs.readFileSync(resolvedPathToSessionData));
}

function getParameter(resolvedPathToSession, key) {
    parameter = readSessionData(resolvedPathToSession + "data.json")['Session'][key];
    if (parameter == null) {
        return UNDEFINED;
    }
    return parameter;
}

function parseIsoTime(timeToParse) {
    const date = timeToParse.split("T")[0];
    const utcTime = timeToParse.split("T")[1].split(".")[0];
    const timeZone = timeToParse.split("T")[1].split("+")[1];

    return date + " " + utcTime + "+" + timeZone;
}

module.exports = {
    getStartTime: function(resolvedPathToSession) {
        return parseIsoTime(getParameter(resolvedPathToSession, 'start_time_iso_with_zone'));
    },

    getStopTime: function(resolvedPathToSession) {
        return getParameter(resolvedPathToSession, 'stop_time_iso_with_zone');
    },

    getPhase: function(resolvedPathToSession) {
        return mission_plan.getPhaseMarkdownLink(getParameter(resolvedPathToSession, 'phase'));
    },

    getStatus: function(resolvedPathToSession) {
        status = getParameter(resolvedPathToSession, 'status');
        switch(status) {
            case STATUS_PLANNED:
                return STATUS_PLANNED_SYM;
            case STATUS_FAILED:
                return STATUS_FAILED_SYM;
            case STATUS_SUCCESS:
                return STATUS_SUCCESS_SYM;
        }
        return status;
    },

    getShortDescription: function(resolvedPathToSession) {
        return getParameter(resolvedPathToSession, 'short_description');
    }
};
