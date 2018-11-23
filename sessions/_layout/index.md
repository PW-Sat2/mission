{% set path = file.path | page_folder %}
{% set tasklist = path + "/tasklist.py" %}
{% set checklistFile = path + "/checklist.json" %}
{% set artifactsFolder = path + "/artifacts" %}
{% set requiredArtifacts = [ "/frames.csv", "/beacons.json" ] %}

{% session_data file.path %}{% endsession_data %}

## Goal
{% block goal %}
MISSING
{% endblock %}

## Checklist
{% checklist "sessions/_layout/checklist.json", checklistFile %}{% endchecklist %}

## Tasklist
{% read_file tasklist %}{%endread_file%}

## Artifacts
{% artifacts artifactsFolder, requiredArtifacts %}{% endartifacts %}
