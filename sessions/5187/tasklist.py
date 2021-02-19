tasks = [
    # Generated on 2021-02-19 23:59:15.955561, contains telemetry from sessions 5186 to 5187.
    # The session starts on 2021-02-20 10:34:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(35, '/telemetry.previous', [1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2050, 2100, 2150, 2200, 2250, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [20, 7, 1, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 1087, 1137, 1187, 1237, 1287]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1057]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [2107, 2157, 2207, 2257, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481, 1531, 1581]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1093, 1143, 1193, 1243, 1293, 1343, 1393]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p1_n_480_0', [0, 19, 25, 27, 29, 30, 31, 32, 33, 34, 39, 41, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p2_w_480_0', [0, 1, 2, 4, 10, 39, 40, 41, 43, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p1_n_480_0', [57, 59, 60, 64, 65, 80, 81, 93, 94, 95, 96, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p1_w_480_0', [60, 61, 63, 64, 80, 81, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p2_n_480_0', [82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    # missing from previous session end
    
    [tc.DownloadFile(100, '/p1_n_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p1_n_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p1_n_480_0', [i for i in range(140, 156, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(103, '/p1_w_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p1_w_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p1_w_480_0', [i for i in range(140, 149, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(106, '/p2_n_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p2_n_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p2_n_480_0', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(109, '/p2_w_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p2_w_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p2_w_480_0', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p2_w_480_0', [i for i in range(160, 171, 1)]), Send, WaitMode.Wait],

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]