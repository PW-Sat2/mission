# LEOP Phase

[LEOP](https://en.wikipedia.org/wiki/Launch_and_Early_Orbit_phase) (Launch and Early Orbit Phase) is fully autonomous. After separation from the launch vehicle it performs a few hardcoded tasks.

| **Mission Time** | **Executed by OBC** | **Comment** |
|-|-|-|
| ~T+0 | `LEOP Experiment` is started. | Gyroscope sampling with 1sps. Saving to `/leop` file. |
| T+40min | `Antenna Deployment Process` starts antenna deployment. | This process should take max 2h. |
| ~T+2h | Starts transmitting `Beacons`. iMTQ starts built-in detumbling. | It is started when `Antenna Deployment Process` was finished. |
| T+4h | `LEOP Experiment` is terminated. Stop iMTQ detumbling. | During [bus commissioning](/mission_plan/bus_commissioning/index.md) download both `/leop` and `/leop_telemetry` files. |
