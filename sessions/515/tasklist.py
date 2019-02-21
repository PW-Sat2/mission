tasks = [
    # Generated on 2019-02-21 14:48:54.871293, contains telemetry from sessions 514 to 515.
    # The session starts on 2019-02-21 19:59:49+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 1563, 1613, 1663, 1713, 1763]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [8, 58, 108, 33, 83, 133, 21, 71, 121, 45, 95, 145, 15, 65, 115, 27, 77, 127, 39, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2051, 2101, 2151, 2201, 2251, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1557, 1607, 1657, 1707, 1757]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2069, 2119, 2169, 2219, 2269, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [139, 1, 51, 101, 151]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]