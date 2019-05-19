tasks = [
    # Generated on 2019-05-19 10:30:28.536000, contains telemetry from sessions 1085 to 1088.
    # The session starts on 2019-05-19 11:49:54+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1407, 1457]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 27, 77, 127, 177, 227, 277, 327, 377]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1395, 1445, 1495, 1545]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [427, 477, 527, 577, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 39, 89, 139, 189]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1419, 1469, 1519, 1569, 1619, 1669]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [239, 289, 339, 389, 439, 489, 539, 9, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 33, 83, 133, 183, 233, 283, 333, 383, 433]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2013, 2063, 2113, 2163, 2213, 2263, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [483, 533, 583, 45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # SunS experiment data download
    [tc.DownloadFile(46, '/suns_ps_4', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_4', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_4', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_4', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_4', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_4', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_4', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_4', [i for i in range(175, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_4', [i for i in range(200, 225, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_4', [i for i in range(225, 250, 1)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]