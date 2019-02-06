tasks = [
    # Generated on 2019-02-06 01:25:18.720000, contains telemetry from sessions 411 to 417.
    # The session starts on 2019-02-06 20:24:02+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1575, 1625, 1675, 1725, 1775]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770, 45, 95, 145, 195]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 33, 83, 133, 183, 233, 283, 333, 383, 433]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2063, 2113, 2163, 2213, 2263, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1557]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333, 1383, 1433]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1483, 1533, 1583, 1633, 1683, 1733, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1707, 1757, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1569, 1619, 1669, 1719, 1769, 1819]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 39, 89, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1189, 1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739, 1, 51, 101, 151, 201, 251, 301, 351]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2131, 2181, 2231, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1613, 1663, 1713, 1763]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]