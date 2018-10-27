CAMs commissioning jest zahardkodowany w OBC i wykonywany jest na telekomendę z GS w trybie eksperymentu lub może być wywołany przez OBC w trakcie [PLD commissioning](mission_plan/commissioning/pld.md). Poniżej przedstawiono sekwencję komend wykonywaną przez OBC.

CAMnadir/CAMwing quick check
==
OBC internal commands sequence **10x repat for each camera**:
* Send a command to EPS: "Enable CAMnadir LCL" to controller A.
* Wait 2s.
* Synchronising the uCAM-II camera in conformance with the [datasheet](https://team.pw-sat.pl/diffusion/PWSAT/browse/cam/_doc/cam_datasheet_4d-systems_serial-camera-module-ucam-ii.pdf), chapter "7.1. Synchronising the uCAM-II". Save in Flash memory (as experiment data) the counted attempts until to first successed SYNC. If there is no SYNC - this is not an error which interrupts next SYNC attempts.
* Send a command to EPS: "Disable CAMnadir LCL" to controller A.

CAMs quick check output data
==
There are 20 of numbers in range between 0..60 or FAIL (a FAIL may be presented as -1 or other well defined value), this mens that there are 20 x int8_t numbers.

CAM Photo test
==
After a quick check, a photo test should be run. There is a 'photo' command in OBC terminal that takes photos from each camera in three resolutions (128, 240 and 480 px) and saves to separate files. Such procedure should be run at this phase. 

# Sample code

```python
{% include "code.py" %}
```
