tasks = [
    # Generated on 2019-05-05 08:22:35.084411, contains telemetry from sessions 1002 to 1003.
    # The session starts on 2019-05-05 09:43:26+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1412, 1462]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [7, 57, 107, 157, 207, 32, 82, 132, 182, 232, 20, 70, 120, 170, 220, 44, 94, 144, 194, 244]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1400, 1450, 1500, 1550]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1424, 1474, 1524, 1574, 1624, 1674]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [14, 64, 114, 164, 214, 26, 76, 126, 176, 226, 38, 88, 138, 188, 238, 0, 50, 100, 150, 200]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2018, 2068, 2118, 2168, 2218, 2268, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2130, 2180, 2230]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(40, '/telemetry.current', [1233, 1283, 1333, 1383]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/radfet_12', [0, 3, 4, 5, 8, 11, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p5_128_0', [20, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p8_128_0', [24, 25, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p9_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p9_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p9_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 51, 52, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p9_480_0', [56, 57, 59, 60, 63, 64, 65, 66, 67, 68, 69, 80, 83, 84, 87, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p3_480_0', [6, 9, 15, 16, 17, 18, 21, 22, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p3_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p3_480_0', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p3_480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    [tc.DownloadFile(60, '/p10_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p10_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p10_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p10_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p10_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p10_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p2_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p2_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p2_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p2_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p2_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p2_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p2_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p2_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p2_480_0', [162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/p8_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p8_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/p8_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p8_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/p8_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p8_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p8_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p8_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p8_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]