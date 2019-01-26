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
    [tc.DownloadFile(30, '/telemetry.previous', [1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 1534, 1584, 1634, 1684]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [29, 79, 129, 179, 229, 279, 4, 54, 104, 154, 204, 254, 42, 92, 142, 192, 242, 292, 16, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1972, 2022, 2072, 2122, 2172, 2222, 2272, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2196, 2246, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1528, 1578]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [116, 166, 216, 266, 36, 86, 136, 186, 236, 286, 48, 98, 148, 198, 248, 10, 60, 110, 160, 210]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1540, 1590, 1640, 1690, 1740, 1790]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [260, 22, 72, 122, 172, 222, 272]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2102, 2152, 2202, 2252]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # Low res photos download
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],

    # High res photos download
    [tc.DownloadFile(110, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p2_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p2_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/p2_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p2_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/p2_480_0', [i for i in range(120, 127, 1)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(117, '/p3_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/p3_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/p3_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/p3_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/p3_480_0', [i for i in range(80, 89, 1)]), Send, WaitMode.Wait],

    # Remove downloaded low photos
    [tc.RemoveFile(200, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(205, '/p6_128_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]