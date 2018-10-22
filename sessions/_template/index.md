{% set name = file.path | page_folder %}
{% set tasklist = "sessions/" + name + "/tasklist.py" %}

# Session: {{ page.title }}

## Goal
{% block goal %}
MISSING
{% endblock %}

## Checklist
{% include "./checklist.md" %}

## Tasklist
{% read_file tasklist %}{%endread_file%}