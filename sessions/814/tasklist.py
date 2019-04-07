tasks = [
    # Generated on 2019-04-07 10:17:13.337000, contains telemetry from sessions 812 to 814.
    # The session starts on 2019-04-07 11:30:27+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # third post-sail SunS experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_3'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1587, 1637, 1687, 1737, 1787]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 7, 57, 107, 157, 207, 257, 307, 357]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [407, 457, 507, 557, 45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 19, 69, 119, 169, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2125, 2175, 2225, 2275, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 1569, 1619]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [269, 319, 369, 419, 469, 519, 569, 39, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 1]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1581, 1631, 1681, 1731, 1781, 1831, 1881]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1931, 1981, 2031, 2081, 2131, 2181, 2231, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 13, 63, 113, 163, 213, 263, 313, 363, 413]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2243, 1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [463, 513, 563, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(50, '/p7_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p8_480_0', [100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 117, 118, 119, 120, 121]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p8_480_0', [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]