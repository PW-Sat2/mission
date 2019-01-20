tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1657, 1707, 1757, 1807, 1857, 1907, 1957]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2, 52, 102, 152, 202, 252, 302, 352, 402, 27, 77, 127, 177, 227, 277, 327, 377, 15, 65, 115]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2007, 2057, 2107, 2157, 2207, 2257, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1669]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [165, 215, 265, 315, 365, 415, 39, 89, 139, 189, 239, 289, 339, 389, 9, 59, 109, 159, 209, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2039, 2089, 2139, 2189, 2239, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1663, 1713]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [309, 359, 409, 21, 71, 121, 171, 221, 271, 321, 371, 33, 83, 133, 183, 233, 283, 333, 383, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [95, 145, 195, 245, 295, 345, 395]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # hi-res focie
    # focia 1 hi-res
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p1_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p1_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p1_480_0', [i for i in range(92, 115, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_480_0', [i for i in range(115, 139, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 2 hi-res
    [tc.DownloadFile(70, '/p2_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p2_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p2_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p2_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p2_480_0', [i for i in range(92, 109, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove already downloaded small photos
    [tc.RemoveFile(200, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_128_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(205, '/p6_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(206, '/p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(207, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/p10_128_0'), Send, WaitMode.Wait],
    
    [tc.ListFiles(210, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]