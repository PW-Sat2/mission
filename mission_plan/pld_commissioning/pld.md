PLD commissioning jest zahardkodowany w OBC i wykonywany jest na telekomendę z GS w trybie eksperymentu. Poniżej przedstawiono sekwencję komend wykonywaną przez OBC. Wszystkie dane zbierane są jako dane eksperymentu.

PLD board quick check
==
OBC internal commands sequence:
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Enable SENS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Wait 10s
* Request, read and save PLD telemetry: payload who, temps, house, suns, photo
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Disable SENS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A

RadFET quick check
==
OBC internal commands sequence:
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Enable SENS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Wait 2 s
* Request, read and save PLD telemetry: payload who, temps, house
* Request, read and save PLD telemetry: radfet on - output data are useless but should be saved
* Wait 10 s
* Request, read and save PLD telemetry: payload radfet read - it takes tens of seconds
* Request, read and save PLD telemetry: payload who, temps, house
* Request, read and save PLD telemetry: radfet off  - just LCL state flag is useful but all output data should be saved
* Wait 2s
* Request, read and save PLD telemetry: radfet read - just to be sure that LCL is off, save all output data
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Disable SENS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A

CAMnadir/CAMwing quick check
==
OBC internal commands sequence:
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Enable CAMnadir](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Wait 10s
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Request, read and save PLD telemetry: payload temps
* Send a command to EPS: [Disable CAMnadir](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Enable CAMwing](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Wait 10s
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Request, read and save PLD telemetry: payload temps
* Send a command to EPS: [Disable CAMwing](https://team.pw-sat.pl/w/eps/lcl/) to controller A

CAMs commssioning
==
Call the [CAMs commissioning](commissioning/cams.md) procedure

SunS commisioning
==
OBC internal commands sequence:
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Enable SunS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A
* Wait 2s
* Trigger SunS measurement with parameters `gain: 0`, `itime: 10` and save data to file (from all SunS registers)
* Save EPS A/B and OBC [telemetry](https://team.pw-sat.pl/w/obc/telemetry/) snapshot
* Send a command to EPS: [Disable SunS LCL](https://team.pw-sat.pl/w/eps/lcl/) to controller A
