tasks = [
    # Generated on 2019-05-19 09:18:10.656000, contains telemetry from sessions 1085 to 1087.
    # The session starts on 2019-05-19 10:15:05+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1407, 1457]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 252, 302, 352, 402, 27, 77, 127, 177, 227, 277, 327, 377, 15, 65, 115]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1395, 1445, 1495, 1545]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1419, 1469, 1519, 1569, 1619, 1669]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [165, 215, 265, 315, 365, 415, 39, 89, 139, 189, 239, 289, 339, 389, 9, 59, 109, 159, 209, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [309, 359, 409, 21, 71, 121, 171, 221, 271, 321, 371, 33, 83, 133, 183, 233, 283, 333, 383, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2013, 2063, 2113, 2163, 2213, 2263, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [95, 145, 195, 245, 295, 345, 395]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # fourth post-sail SunS experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_4'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]