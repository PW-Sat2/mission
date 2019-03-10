tasks = [
    # Generated on 2019-03-10 08:19:05.772000, contains telemetry from sessions 625 to 628.
    # The session starts on 2019-03-10 10:19:06+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2262, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [32, 82, 132, 182, 232, 282, 332, 382, 432, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2237, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2225, 2275, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [95, 145, 195, 245, 295, 345, 395, 445, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 39, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2199, 2249, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2169, 2219, 2269, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [139, 189, 239, 289, 339, 389, 439, 1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 13, 63, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2131, 2181, 2231, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2143, 2193, 2243, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005, 2055, 2105]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [163, 213, 263, 313, 363, 413, 463, 25, 75, 125, 175, 225, 275, 325, 375, 425]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [2155, 2205, 2255]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # High res photos download

    # 'Chunks': 1, 'File': 'p1_480_0'
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 1, 1)]), Send, WaitMode.Wait],

    # 'Chunks': 144, 'File': 'p2_480_0'
    [tc.DownloadFile(70, '/p2_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p2_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p2_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p2_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p2_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p2_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p2_480_0', [i for i in range(129, 144, 1)]), Send, WaitMode.Wait],

    # 'Chunks': 156, 'File': 'p3_480_0'
    [tc.DownloadFile(80, '/p3_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p3_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p3_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p3_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p3_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p3_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p3_480_0', [i for i in range(129, 156, 1)]), Send, WaitMode.Wait],

    # 'Chunks': 88, 'File': 'p7_480_0'
    [tc.DownloadFile(90, '/p7_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/p7_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/p7_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/p7_480_0', [i for i in range(78, 88, 1)]), Send, WaitMode.Wait],


    # Remove files
    [tc.RemoveFile(100, 'p1_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(102, 'p2_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(104, 'p3_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(106, 'p4_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(108, 'p5_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(110, 'p6_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(112, 'p7_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(114, 'p8_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(116, 'p9_128_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(118, 'p10_128_0'), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]