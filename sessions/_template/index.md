{% set name = file.path | page_folder %}
{% set tasklist = "sessions/" + name + "/tasklist.py" %}
{% set checklistFile = "sessions/" + name + "/checklist.json" %}
{% set artifactsFolder = "sessions/" + name + "/artifacts" %}
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