tasks = [
    # Generated on 2019-06-16 20:37:26.991000, contains telemetry from sessions 1282 to 1285.
    # The session starts on 2019-06-16 21:54:44+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1541, 1591, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1466, 1516, 1566, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1404, 1454, 1504, 1554, 1604, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1328, 1378, 1428, 1478, 1528, 1578, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]