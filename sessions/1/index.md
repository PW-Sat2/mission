{% extends "/sessions/_layout/index.md" %}

{% block goal %}
Trying to find the satellite in orbit and trying to estimate TLE. In as simple as possible way: `PingTelecommand()` in SendLoop to establish a stable radio link, then `SendBeacon()` in SendLoop, to get more telemetry data.
{% endblock %}
