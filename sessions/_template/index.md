{% set path = file.path | page_folder %}
{% set tasklist = path + "/tasklist.py" %}
{% set checklistFile = path + "/checklist.json" %}
{% set artifactsFolder = path + "/artifacts" %}
{% set requiredArtifacts = [ "frames.csv", "beacons.json" ] %}

# Session {{ page.title }}

## Goal
{% block goal %}
MISSING
{% endblock %}

## Checklist
{% checklist "sessions/_template/checklist.json", checklistFile %}{% endchecklist %}

## Tasklist
{% read_file tasklist %}{%endread_file%}

## Artifacts
{% artifacts artifactsFolder, requiredArtifacts %}{% endartifacts %}
