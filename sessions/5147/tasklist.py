tasks = [
    # Generated on 2021-02-12 16:47:56.004771, contains telemetry from sessions 5146 to 5147.
    # The session starts on 2021-02-12 21:24:13+01:00.

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1110, 1160]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1098, 1148, 1198, 1248, 1298]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1642, 1692, 1742, 1792, 1842, 1892, 1942, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1754, 1804, 1854, 1904, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1916, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [917, 924, 930, 936, 942, 948, 954, 960, 967, 974, 980, 986, 992, 998, 1004, 1010, 1017, 1024]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1030, 1036, 1042, 1048, 1054, 1060, 1067, 1074, 1080, 1086, 1092, 1098, 1104, 1110, 1117, 1124, 1130]), Send, WaitMode.Wait],
    # missing from previous session end

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],


    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
