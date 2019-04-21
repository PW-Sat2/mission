tasks = [
    # Generated on 2019-04-21 22:05:27.461751, contains telemetry from sessions 908 to 912.
    # The session starts on 2019-04-21 23:07:33+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1547, 1597, 1647, 1697, 1747, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 584, 634, 684, 734, 784]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1554, 1604, 1654, 1704, 1754, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 590, 640, 690, 740, 790]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    # auto-generated file remove end


    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

     # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

     # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

     # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
