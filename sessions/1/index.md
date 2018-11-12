{% extends "/sessions/_template/index.md" %}

{% block goal %}
Trying to find the satellite in orbit and trying to estimate TLE. In as simple as possible way: `PingTelecommand()` in loop, then `SendBeacon()` and `ListFiles()` telecommands.
{% endblock %}
