SADS experiment from OBC point of view
==
* T+0 - Send a command to iMTQ to enter to Idle Mode (MTQ actuation is disabled).
* T+0 - Send a command to EPS to switch the SENS LCL on (5V supply for PLD board): "enable SENS LCL" to controller A.
* T+1s - Start experiment data recording with 1Hz [TBC] sampling rate: temperature sensors and photodiodes on solar panels, gyroscope readouts (placed on PLD board).
* T+1s - Send a command sequence to EPS to switch main thermal knives on for 2min: "enable TKmain LCL", wait 100ms and "enable TKmain LCL" to controller A, wait 100ms,  "enable SADSmain BURN switch", wait 100ms and  "enable SADSmain BURN switch" to controller A.
* T+2min - Send a command sequence to EPS to switch redundant thermal knives on for 2min: "enable TKmain LCL", wait 100ms and "enable TKmain LCL" to controller B, wait 100ms,  "enable SADSmain BURN switch", wait 100ms and  "enable SADSmain BURN switch" to controller B.
* T+3min - Stop experiment data recording.
* T+4min - Send a command sequence to EPS to switch all thermal knife's LCLs off: "disable TKmain LCL" to controller A and  "disable TKred LCL" to controller B.
* T+4min - Take a photo with CAMwing with high resolution (JPEG 640x480).
* Return to [Survival Mode](https://team.pw-sat.pl/w/oper/satellite_modes).

SADS experiment from OPERation point of view
==
1st communication session:
===
* T+0 - Send a telecommand to start SADS experiment.
* T+3min5s - Send a request for recorded experiment data: temperature sensors and photodiodes on solar panels, gyroscope readouts.
... experiment data receiving, beacon receiving.
NOTE: estimated max contact window duration is about **4 min**, while mean duration is about **3.1 min**

Next communication sessions:
===
* Send requests for high resolution photo from CAMwing.

SADS experiment raw data estimation
==
* Temperature sensors (4*12 bits) and photodiodes (4*12 bits) on solar panels, gyroscope readouts (all sensor registers: 64 bits) with sampling rate 1Hz for 2min: 152 bits * 180 = 27360 bits = 3.3 kB. Estimated download time at 200bps: 137 seconds.
