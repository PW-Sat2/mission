{% set name = file.path | page_folder %}
{% set tasklist = "sessions/" + name + "/tasklist.py" %}
{% set checklistFile = "sessions/" + name + "/checklist.json" %}

# Session: {{ page.title }}

## Goal
{% block goal %}
MISSING
{% endblock %}

## Checklist
{% checklist "sessions/_template/checklist.json", checklistFile %}{% endchecklist %}

## Tasklist
{% read_file tasklist %}{%endread_file%}