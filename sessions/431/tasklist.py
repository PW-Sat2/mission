tasks = [
    # Generated on 2019-02-08 16:13:09.672000, contains telemetry from sessions 427 to 431.
    # The session starts on 2019-02-08 20:33:40+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2256, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [26, 76, 126, 176, 1, 51, 101, 151, 201, 39, 89, 139, 189, 13, 63, 113, 163, 213, 33, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2231, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2219, 2269, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2193, 2243, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2163, 2213, 2263, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [133, 183, 45, 95, 145, 195, 7, 57, 107, 157, 207, 19, 69, 119, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2125, 2175, 2225, 2275, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2087, 2137, 2187, 2237, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2099, 2149, 2199, 2249]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]