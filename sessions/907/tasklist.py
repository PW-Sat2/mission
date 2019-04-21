tasks = [
    # Generated on 2019-04-20 23:38:32.979000, contains telemetry from sessions 905 to 907.
    # The session starts on 2019-04-21 10:39:09+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.previous', [1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1406, 1456]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1, 51, 101, 151, 201, 251, 301, 351, 401, 26, 76, 126, 176, 226, 276, 326, 376, 14, 64, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 1394, 1444, 1494, 1544]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1418, 1468, 1518, 1568, 1618, 1668]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [164, 214, 264, 314, 364, 414, 38, 88, 138, 188, 238, 288, 338, 388, 8, 58, 108, 158, 208, 258]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1388, 1438, 1488, 1538, 1588, 1638, 1688, 1738]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [308, 358, 408, 20, 70, 120, 170, 220, 270, 320, 370, 32, 82, 132, 182, 232, 282, 332, 382, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2012, 2062, 2112, 2162, 2212, 2262, 1424, 1474, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [2124, 2174, 2224, 2274]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [94, 144, 194, 244, 294, 344, 394]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # fourth post-sail SunS experiment
    [tc.PerformSunSExperiment(65, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_4'), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p1_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p1_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(46, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p2_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p2_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p2_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p2_480_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p2_480_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p2_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p2_480_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p7_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p7_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p7_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p7_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p7_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p7_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p7_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p7_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p7_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(63, 'radfet_11'), Send, WaitMode.Wait],
    [tc.ListFiles(64, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]