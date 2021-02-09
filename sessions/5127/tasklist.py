tasks = [
    # Generated on 2021-02-09 11:01:23.474000, contains telemetry from sessions 5126 to 5127.
    # The session starts on 2021-02-09 12:04:23+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(47, '/telemetry.current', [1943, 1993, 2043, 2093, 2143, 1968, 2018, 2068, 2118, 1956, 2006, 2056, 2106, 2156, 1980, 2030, 2080, 2130, 1950, 2000]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [2050, 2100, 2150, 1962, 2012, 2062, 2112, 1974, 2024, 2074, 2124, 1986, 2036, 2086, 2136]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [717, 724, 736, 742, 748, 754, 760, 767, 774, 786, 792, 798, 804, 810, 817, 824, 836, 842]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [848, 854, 860, 867, 874, 886, 892, 898, 904, 910, 917, 924, 936, 942, 948, 954, 960, 967]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [974, 986, 998, 1004, 1010, 1017, 1024, 1036, 1042, 1048, 1054, 1060, 1067, 1074, 1086, 1098, 1104, 1110]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1117, 1124, 1136, 1148, 1154, 1160, 1174, 1180, 1186, 1198, 1204, 1210, 1224, 1230, 1236, 1248, 1254, 1260]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1274, 1280, 1286, 1298, 1304, 1310, 1324, 1330, 1336, 1348, 1354, 1360, 1367, 1374, 1380, 1386, 1398, 1404]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1410, 1424, 1430, 1436, 1442, 1448, 1454, 1460, 1474, 1480, 1486, 1492, 1498, 1504, 1510, 1524, 1530, 1536]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1548, 1554, 1560, 1574, 1580, 1586, 1598, 1604, 1610, 1624, 1630, 1636, 1648, 1654, 1660, 1674, 1680, 1686]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1698, 1704, 1710, 1724, 1730, 1736, 1748, 1754, 1760, 1774, 1780, 1786, 1798, 1804, 1810, 1824, 1830, 1836]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1848, 1854, 1860, 1874, 1880, 1886, 1898, 1904, 1910, 1924, 1930, 1936, 1948, 1954, 1960, 1974, 1980]), Send, WaitMode.Wait],

    [tc.DownloadFile(39, '/l02n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/l02w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/l02n_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/l02n_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/l02n_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/l02w_0', [17, 18, 19, 20, 24, 26, 32, 37, 38, 39, 40, 43, 44, 48, 49, 50, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/l02w_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/l02w_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    # missing from previous session end


    # Missings based on missing parts of photos
    [tc.DownloadFile(82, '/l01n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/l01n_0', range(60, 76)), Send, WaitMode.Wait],

    [tc.DownloadFile(84, '/l01w_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/l01w_0', range(100, 110)), Send, WaitMode.Wait],

    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]