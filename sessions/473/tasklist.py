tasks = [
    # Generated on 2019-02-14 18:01:51.623000, contains telemetry from sessions 469 to 473.
    # The session starts on 2019-02-14 21:01:34+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2132, 2182, 2232, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [2, 52, 27, 77, 15, 65, 39, 89, 9, 59, 21, 71, 33, 83, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2007, 2057, 2107, 2157, 2207, 2257, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1139, 1189, 1239, 1289, 1339, 1389, 1439, 1489]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1151, 1201, 1251, 1301, 1351]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1163, 1213]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2263, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    #Session 469 missings
    [tc.DownloadFile(31, '/telemetry.previous', [15, 33, 133, 147, 183, 233, 265, 283, 333, 377, 383, 465, 471, 483]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [521, 533, 571, 577, 583, 633, 653, 683, 733, 777, 783, 833, 865]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [883, 921, 933, 965, 971, 983, 1021, 1033, 1040, 1071, 1083, 1121, 1133]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]