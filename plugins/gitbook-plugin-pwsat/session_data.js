const fs = require('fs');
const mission_plan = require('./mission_plan');

const UNDEFINED = "[TBD]";

const STATUS_PLANNED = "planned";
const STATUS_FAILED = "failed";
const STATUS_SUCCESS = "success";
const STATUS_AUTO = "auto";

const STATUS_PLANNED_SYM = "<span style='color:orange;font-size:200%' title='Planned'>&#x231A;</span>";
const STATUS_FAILED_SYM = "<span style='color:red;font-size:200%' title='Failed'>&#x2612;</span>";
const STATUS_SUCCESS_SYM = "<span style='color:green;font-size:200%' title='Success'>&#x2611;</span>";
const STATUS_AUTO_SYM = "<span style='color:gray;font-size:200%' title='Auto'>&#x1F916;</span>";

function readSessionData(resolvedPathToSessionData) {
    try {
        return JSON.parse(fs.readFileSync(resolvedPathToSessionData));
    }
    catch (error) {
        return {};
    }
}

function getParameter(resolvedPathToSession, key) {
    try {
        parameter = readSessionData(resolvedPathToSession + "data.json")['Session'][key];
        if (parameter == null) {
            return UNDEFINED;
        }
        return parameter;
    }
    catch (error) {
        return UNDEFINED;
    }
}

function parseIsoTime(timeToParse) {
    try {
        const date = timeToParse.split("T")[0];
        const utcTime = timeToParse.split("T")[1].split(".")[0].split("+")[0];
        const timeZone = timeToParse.split("T")[1].split("+")[1];

        if (date.length != 10) { throw "DateError"; }
        if (utcTime.length < 5) { throw "TimeError"; }
        if (timeZone.length < 5) { throw "ZoneError"; }

        return date + " " + utcTime + "+" + timeZone;
    } 
    catch (error) {
        return UNDEFINED;
    }
}

module.exports = {
    getStartTime: function(resolvedPathToSession) {
        return parseIsoTime(getParameter(resolvedPathToSession, 'start_time_iso_with_zone'));
    },

    getStopTime: function(resolvedPathToSession) {
        return parseIsoTime(getParameter(resolvedPathToSession, 'stop_time_iso_with_zone'));
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
            case STATUS_AUTO:
                return STATUS_AUTO_SYM;
        }
        return UNDEFINED;
    },

    getShortDescription: function(resolvedPathToSession) {
        shortDescription = getParameter(resolvedPathToSession, 'short_description');
        if (shortDescription.length == 0) {
            return UNDEFINED;
        }
        return shortDescription;
    },

    process: function(block) {
        const sessionIndexFilePath = block.args[0];
        const sessionDir = sessionIndexFilePath.replace("index.md", "");

        const index = sessionDir.split('/').slice(-2)[0];
        const startTime = module.exports.getStartTime(sessionDir);
        const stopTime = module.exports.getStopTime(sessionDir);
        const phase = module.exports.getPhase(sessionDir);
        const status =  module.exports.getStatus(sessionDir);
        const description = module.exports.getShortDescription(sessionDir);

        sessionDataTable = [
            `|**Index**|**Start Time**|**Stop Time**|**Phase**|**Status**|**Short description**|`,
            `|:-:|:-:|:-:|:-:|:-:|:-|`,
            `|${index}|${startTime}|${stopTime}|${phase}|${status}|${description}|`
        ]

        return {
            body: sessionDataTable.join('\n'),
            parse: true
        }
    }
};
