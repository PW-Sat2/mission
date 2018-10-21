Timeline, experiment phases and goals
=

**Top-level timeline of the PW-Sat2 is described in [[ oper/mission_plan/ | Mission Plan ]] document. Description below contains more detailed information, however it's more likely to be changed in near future.**

Phase 1: T+7d - T+11d
---
**The basic time slot for experiment.**

**T+7d**
1st communication session:
- SunS experiment turned on for the **first time**

**T+8d**
2nd communication session:
- SunS experiment turned on for **second time**
- Receive primary data (log file) from the first run of experiment

**T+9d**
3rd communication session:
- SunS experiment turned on for **third time**
- Receive primary data (log file) from the second run of experiment

**T+10d**
4th communication session:
- SunS experiment turned on for **fourth time**
- Receive primary data (log file) from the third run of experiment

**T+11d**
- Receive primary data (log file) from the fourth run of the experiment

**For each day**
During spare communication session there are possible following actions (decisions up to #oper)
- retransmit primary data (if needed)
- download secondary data (if needed)
- send //extra //data

Phase 2: T+22d - T+23d
---
This phase should be run by the #oper once the first Sun Pointing experiment is finished and default detumbling is turned on (iMTQ built-in). During this phase the satellite is expected to have some angular velocity, hence it's suitable to test the SunS in non-stationary conditions.

**T+22**
1st communication session:
- SunS experiment turned on

**T+23**
2nd communication session:
- Receive primary data (log file)

Phase 3: T+35d - T+36d
---

This phase is intended to check long term survival of the sensor on orbit. The key parameter to examine is durability to high doses of ionizing radiation (TID).

**T+35d**
1st communication session:
- SunS experiment turned on

**T+36d**
2nd communication session:
- Receive primary data (log file)


Data acquisition
=

The SunS has 67 byte long register map that can be read. However as a primary data, the range of 0 - 40 bytes is taken into account. Data in this range will be saved as a primary SunS experiment data log (a file). Data in range 41 - 66 bytes should be also saved as a secondary data log (separate file). These secondary data will be transferred if needed (e.g. in case of problems with primary data or during additional communication sessions).

There are several sensors to be sampled along with the SunS, namely:
* Reference Sun Sensor - raw data from ADC
* Gyroscope (raw data: X, Y, Z, Temperature)

Each sensor should be sampled every time data from the SunS  are acquired, so the sample rate is common for all the sensors in the experiment. A set of data containing one sample of each desired sensor is called the **data set**. The data set is a primary data log from the experiment.

Detailed description of data files format used on OBC can be found on [GitHub](https://github.com/PW-Sat2/PWSat2OBC/wiki/Data-handling-%26-packet-format#file-storage).

| id primary data | primary data (the data set) |
| id secondary data | Data from 41 - 66 bytes of the SunS registers |

It's expected that each run of the experiment will be saved in separate file, therefore IDs have to be different. They should be send by #oper in telecommand turning on the experiment.

The primary and secondary data sets
---
Primary data set
| **#** | **Field Name** | **Size [bytes]** |
| 1 | Timestamp | 8 |
|  2 | The SunS (registers 0 - 40 | 41 |
| 3 | Reference Sun Sensor | 10 |
| 4 | Gyroscope | 8 |
|   |  **Sum** | **67** |

Secondary data set

| **#** | **Field Name** | **Size [bytes]** |
| 1 | Timestamp | 8 |
|  2 | The SunS (registers 41 - 66) | 26 |
|   |  **Sum** | **34** |

Radio link budget
---
Each run of the SunS experiment is planned in such a way that it's possible to download almost all data from primary log file in a single communication session. However, the experiment will generate slightly more data that can be downloaded during spare communication sessions.

** Link budget calculations**

* Useful time of each session: **200 s**
* Real data rate: **300 b/s**

**Amount of data in one session: 7.5 kB**
**Number of data sets that can be sent in one session: 111**

Specification of each run of the experiment
===
Due to needs for high reliability of system, limited amount of time for development  and testing, some simplifications have to be implemented. Therefore, **each run of the SunS experiment is exactly the same**.

Input parameters for experiment provided via telecommand are:
* `gain` - a parameter of the SunS [`uint8_t`, unit: `raw`]
* `itime` - a parameter of the SunS [`uint8_t`, unit: `raw`]
* `samples_qty` - number of samples to be acquired in fast sampling mode [`uint8_t`, unit: `n/a`]
* `short_delay` - delay between consecutive samples in fast sampling mode [`uint8_t`, unit: `seconds`]
* `qty_of_sampling_sessions` - number of fast sampling sessions [`uint8_t`, unit: `n/a`]
* `long_delay` - delay between fast sampling sessions [`uint8_t`, unit: `minutes`]
* 'filename_base' - base filename for the SunS experiment files


Description for OBC Team
===

Sequence (pseudocode):
---

```
begin_experimet()

for i in range(qty_of_sampling_sessions):
    turn_on_equipment();

    for j in range(samples_qty):
        take_sample_from_all_sensors()
        delay_seconds(short_delay)
    delay_minutes(long_delay)

    turn_off_equipment();
end_experiment()

```

Definitions
---

`begin_experimet()`:

* create two files for experiment data with basename `filename_base`

`turn_on_equipment()`:

* enable payload: `eps enable_lcl SENS`
* enable the SunS: `eps enable_lcl SUNS`
* initialize gyroscope (?)
* delay_seconds(3)

`turn_off_equipment()`:

* disable payload: `eps disable_lcl SENS`
* disable the SunS: `eps disable_lcl SUNS`

`end_experimet()`:

* enable payload: `eps disable_lcl SENS`
* disable the SunS: `eps disable_lcl SUNS`

Failures
===
In case of any failure of SunS OBC keeps trying to communicate with a device according to the schedule. If a trial fails, zeroes should be written to a memory (file). Frankly speaking, OBC should ignore all errors.

Description for #OPER
===


Experiment checklist and success levels
===
