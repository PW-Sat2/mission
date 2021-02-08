tasks = [
    # Generated on 2021-02-08 23:49:17.354004, contains telemetry from sessions 5125 to 5126.
    # The session starts on 2021-02-09 10:33:28+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(66, '/telemetry.current', [717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [1717, 1767, 1817, 1867, 1917, 1967, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 730, 780, 830, 880, 930, 980, 1030, 1080, 1130]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [1180, 1230, 1280, 1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 754, 804, 854]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [1904, 1954, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 748, 798, 848, 898, 948, 998, 1048]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [1098, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 760, 810]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [1860, 1910, 1960]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/l01w_0', [0, 1, 2, 4, 8, 10, 11, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/l01n_0', [9, 10, 20, 21, 22, 23, 24, 25, 29, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/l02w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/l02w_0', range(21, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/l02w_0', range(41, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/l02w_0', range(61, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/l02w_0', range(81, 86)), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/l02n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/l02n_0', range(21, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/l02n_0', range(41, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/l02n_0', range(61, 74)), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end

    tc.RemoveFile(41, '/l01w_0'), Send, WaitMode.Wait],
    tc.RemoveFile(42, '/l01n_0'), Send, WaitMode.Wait],
    tc.RemoveFile(43, '/l02w_0'), Send, WaitMode.Wait],
    tc.RemoveFile(44, '/l02n_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]