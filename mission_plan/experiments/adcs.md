# NIE MA ADCSu

IMPORTANT: DO NOT TURN ON ADCS Detumbling experiment! It's harmful to satellite's power budget and may cause an overheat!

Detumbling experiment
==

Detumbling experiment from OBC point of view:
* T+0 - Send a command to iMTQ to enter to Idle Mode (to actuate with magnetotorquers).
* T+0 - Send a command to EPS to switch the SENS LCL on (5V supply for PLD board): "enable SENS LCL" to controller A.
* T+2s - Start experiment data recording with selected (as a parameter in a telecommand) sampling rate - resolution of 1 s, `uint8_t`.
Data to be recorded: timestamp, temperature sensors (payload temps like), photodiodes (payload photo like) on solar panels, gyroscope readouts (placed on PLD board), iMTQ magnetometer, iMTQ torque dipols, SunSref. All data in raw form.
* T+2s - Start selected algorithm for a selected time (as a parameter in a telecommand) - units: minutes, `uint8_t`.
* T+[time] - Stop experiment data recording.
* T+[time]+1s - Send a command to EPS to switch the SENS LCL off (5V supply for PLD board): "disable SENS LCL" to controller A.
* Return to [Survival Mode](https://team.pw-sat.pl/w/oper/satellite_modes).

All recorded data are stored as a experiment data file.
