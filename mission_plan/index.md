[LEOP](https://en.wikipedia.org/wiki/Launch_and_Early_Orbit_phase)
==

**T+0:**

* QuadPack deploy
* EPS ON
* OBC ON
* COMM RX ON
* iMTQ idle
* Start saving telemetry every 1min

**T+1min:**
* Start LEOP experiment: gyroscopes acquisition with high sample rate (1 sps)

**T+1min - T+40min**
* Just wait, nothing to do

**T+40min - T+2h**
* [Antenna deployment procedure](leop/antenna_deployment_procedure.md).
* After antenna deployment:
** enable telemetry downlink,
** turn on iMTQ, perform self-test and enable detumbling.

**T+4h**
* Stop LEOP experiment.
* Copy `telemetry.current` file to `leop_telemetry` file.
* Turn off iMTQ permanently.

-------------------

BUS Commissioning
==

**T+4h - T+4day:**
* Satellite signal aquisition and TLE estimation.
* [TM] on-line telemetry downlink.
* [TC] Files list downloading.
* [TC] Request parts of historical telemetry (`telemetry.current`, `telemetry.previous`).
* [TC] Download parts of `leop_telemetry`, `leop` files.

-------------------

PLD Commissioning
==

**T+4day - T+7day:**

* [TC] [PLD commissioning](commissioning/pld.md).
* [TC] Files list downloading.
* [TC] PLD commissioning files downloading and deleting.

-------------------

Experiments
==

**T+7day - T+11day**
* [TC] Higher downlink baudrate test: 9600bps. If it is OK -> next sessions with higher baudrate.
* [TC] PLD commissioning files downloading to test new baudrate.

**T+11day - T+18day**

* [TC] [SunS experiment](experiments/suns.md)
* [TC] Files list downloading.
* [TC] SunS experiment files downloading and deleting.

**T+18day - T+25day**
* [TC] CAMs photos taking and downloading.

-------------------

Extended Mission
==

**T+25day - T+27day**
* [TC] [RadFET experiment](experiments/redfet.md)
* [TC] RadFET experiment files downloading.

**T+28day - T+33day**
* [TC] [CAMs commissioning](commissioning/cams.md) and CAMs photos.
* [TC] Photos downloading.

**T+33day - T+36day**
* [TC] [SunS experiment](experiments/suns.md)
* [TC] SunS experiment files downloading.

**T+36day - T+38day**
* [TC] [SADS experiment](experiments/sads.md)
* [TC] SADS experiment files downloading.

SAIL Experiment {icon bolt}
==

**T+39day - [TBD]**

* [TC] [SAIL experiment](experiments/sads.md)

**T+40day**

* Emergency SAIL deployment (hardcoded task) {icon fire}

-------------------

Activity after SAIL deployment
==

**SAIL Experiment files downloading**
* [TM] Beacons receiving.
* [TC] [SAIL experiment](experiments/sads.md) files downloading.
