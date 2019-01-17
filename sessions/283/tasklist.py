tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1419, 1469]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 1464, 1514, 1564, 1614, 39, 89, 139, 189, 239, 289, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1407, 1457, 1507, 1557]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189, 1239, 1289, 1339]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1389, 1439, 1489, 1539, 1589, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1431, 1481, 1531, 1581, 1631, 1681]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1, 51, 101]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1521, 1571, 1621, 33, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1963, 2013, 2063, 2113, 2163, 2213, 2263, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 45, 95, 145, 195, 245]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2075, 2125, 2175, 2225, 2275, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1295, 1345, 1395, 1445, 1495, 1545, 1595, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [2187, 2237]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 3 hi-res - missings
    [tc.DownloadFile(100, '/p3_480_0', [28, 31, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/p3_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove already downloaded small and big photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(200, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_128_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(205, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(206, '/p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(207, '/p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p5_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(210, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
