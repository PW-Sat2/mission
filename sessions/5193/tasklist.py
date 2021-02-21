tasks = [
    # Generated on 2021-02-21 08:55:14.434000, contains telemetry from sessions 5192 to 5193.
    # The session starts on 2021-02-21 10:54:12+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.previous', [1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1465, 1515, 1565]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [10, 60, 110, 160, 210, 260, 310, 360, 35, 85, 135, 185, 235, 285, 335, 385, 23, 73, 123, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1453, 1503, 1553, 1603, 1653, 1703]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [223, 273, 323, 373, 47, 97, 147, 197, 247, 297, 347, 397, 17, 67, 117, 167, 217, 267, 317, 367]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [2047, 2097, 2147, 2197, 2247, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [2209, 2259, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1483]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [29, 79, 129, 179, 229, 279, 329, 379, 41, 91, 141, 191, 241, 291, 341, 391, 3, 53, 103, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [203, 253, 303, 353, 403]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(34, '/pw_p0_0', [49, 50, 51, 53, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pw_p1_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pw_p1_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    # missing from previous session end


    [tc.DownloadFile(100, '/pw_p6_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/pw_p10_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/pw_p14_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/pw_p19_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/pw_p10_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/pw_p19_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],

    [tc.DownloadFile(108, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/pw_p10_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/pw_p19_0', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],

    [tc.DownloadFile(112, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/pw_p10_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],

    [tc.DownloadFile(116, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],


    [tc.RemoveFile(77, 'n01n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(78, 'n01w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(79, 'n02n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(80, 'n02w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(81, 'p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(82, 'p1_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(83, 'p1_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(84, 'p1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(85, 'p2_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(86, 'p2_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(87, 'p5174_0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(88, 'p5174_1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(89, 'radfet_60'), Send, WaitMode.Wait],
    [tc.RemoveFile(90, 'radfet_61'), Send, WaitMode.Wait],
    [tc.ListFiles(91, '/'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]