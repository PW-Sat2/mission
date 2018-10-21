SAIL experiment from OBC point of view
==
* T+0 - Send a command to iMTQ to enter to Idle Mode (MTQ actuation is disabled).
* T+0 - Send a command to EPS to switch the SENS LCL on (5V supply for PLD board): "enable SENS LCL" to controller A.
* T+1s - Start experiment data recording with 1Hz [TBC] sampling rate: SRM (Sail Release Mechanism) temperature and switch state, gyroscope readouts (placed on PLD board).
* T+1s - Send a command sequence to EPS to switch main thermal knives on for 2min: 
** "enable TKmain LCL" to controller A, 
** wait 100ms,
** "enable TKmain LCL" to controller A, 
** wait 100ms,  
** "enable SAILmain BURN switch" to controller A, 
** wait 100ms,
** "enable SAILmain BURN switch" to controller A.
* T+1s - Start CAMwing and CAMnadir images taking with low resolution (JPEG 160x128) with 2.5s between each photo. Cameras are switched on commutatively/interchangeably: CAMnadir photo, wait 2.5s, CAMwing photo, wait 2.5s...
* T+2min - Send a command sequence to EPS to switch main thermal knife's LCLs off: 
** "disable TKmain LCL" to controller A.
** wait 100ms,
** "disable TKmain LCL" to controller A.
* T+2min - Send a command sequence to EPS to switch redundant thermal knives on for 2min: 
** "enable TKred LCL" to controller B, 
** wait 100ms,
** "enable TKred LCL" to controller B,
** wait 100ms,
** "enable SAILred BURN switch" to controller B, 
** wait 100ms,
** "enable SAILred BURN switch" to controller B.
* T+4min - Stop experiment data recording.
* T+4min - Send a command sequence to EPS to switch redundant thermal knife's LCLs off: 
** "disable TKred LCL" to controller B.
** wait 100ms,
** "disable TKred LCL" to controller B.
* T+4min - Take two photos with both CAMnadir and CAMwing cameras with high resolution (JPEG 640x480).
* Return to [Survival Mode](https://team.pw-sat.pl/w/oper/satellite_modes).

SAIL experiment from OPERation point of view
==
1st communication session:
===
* T+0 - Send a telecommand to start SAIL experiment.
* T+2min5s - Send a request for recorded experiment data: SRM temperature and switch state, gyroscope readouts.
NOTE: estimated max contact window duration is about **4 min**, while mean duration is about **3.1 min**

* T+>3min... experiment data receiving, beacon receiving.

Next communication sessions:
===
* Send requests for high resolution photo from CAMnadir.
* Send requests for every fifth low resolution photo from selected camera (or both).
* Send requests for selected low resolution photos from selected camera (or both).
* Send requests for rest of the low resolution photos.
* Send requests for high resolution photo from CAMwing.

SAIL experiment raw data estimation
==
* SRM temperature (12 bit)
* switch state (1 bit)
* gyroscope readouts (all sensor registers: 64 bits) with sampling rate 1 Hz for 4 min
* 77 bits/s * 240 s = 18480 bits = 2.34 kB. 
* Estimated download time at 200 bps: 92 seconds.
