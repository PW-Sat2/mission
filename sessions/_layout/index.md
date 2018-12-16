{% set path = file.path | page_folder %}
{% set tasklist = path + "/tasklist.py" %}
{% set checklistFile = path + "/checklist.json" %}
{% set artifactsFolder = path + "/artifacts" %}
{% set requiredArtifacts = [ "all.frames", "fp-gs_downlink.frames", "elka_downlink.frames", "beacons.txt", "downlink_frames.txt" ] %}

{% session_data file.path %}{% endsession_data %}

## Goal
{% block goal %}
MISSING
{% endblock %}

## Tasklist
{% read_file tasklist %}{%endread_file%}

## Artifacts
{% artifacts artifactsFolder, requiredArtifacts %}{% endartifacts %}
