tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 38, 88, 138, 188, 238, 288, 338]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2118, 2168, 2218, 2268, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 1730, 1780, 1830, 1880]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [388, 438, 488, 538, 588, 638, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 0]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1930, 1980, 2030, 2080, 2130, 2180, 2230, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1712]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 20, 70, 120, 170, 220, 270, 320]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [370, 420, 470, 520, 570, 620, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2174, 2224, 2274, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 6, 56, 106, 156, 206, 256, 306, 356]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [406, 456, 506, 556, 606]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # Two high res photos download
    [tc.DownloadFile(100, '/p1_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p1_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p1_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p1_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p1_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p1_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p1_480_0', [i for i in range(120, 145, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(107, '/p5_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p5_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p5_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p5_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p5_480_0', [i for i in range(80, 93, 1)]), Send, WaitMode.Wait],
    
    # Remove downloaded photos
    [tc.RemoveFile(211, '/p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/p7_480_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]