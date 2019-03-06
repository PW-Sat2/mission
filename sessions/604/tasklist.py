tasks = [
    # Generated on 2019-03-06 17:58:59.388000, contains telemetry from sessions 600 to 604.
    # The session starts on 2019-03-06 20:56:12+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2276, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [46, 96, 146, 196, 21, 71, 121, 171, 221, 9, 59, 109, 159, 209, 33, 83, 133, 183, 233, 3]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2251, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2239, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2263, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2233, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [53, 103, 153, 203, 15, 65, 115, 165, 215, 27, 77, 127, 177, 227, 39, 89, 139, 189]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2245, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2257, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2269]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]