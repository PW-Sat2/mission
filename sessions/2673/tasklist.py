tasks = [
    # Generated on 2020-01-20 09:07:09.909000, contains telemetry from sessions 2671 to 2673.
    # The session starts on 2020-01-20 09:43:04+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 1568, 1618, 1668, 1718, 1768]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 38, 88, 138, 188, 238, 288, 338, 388]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [438, 488, 538, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 0, 50, 100, 150, 200, 250]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2056, 2106, 2156, 2206, 2256, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1550]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [300, 350, 400, 450, 500, 550, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 32, 82, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1562, 1612, 1662, 1712, 1762, 1812]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [182, 232, 282, 332, 382, 432, 482, 532, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2124, 2174, 2224, 2274, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [56, 106, 156, 206, 256, 306, 356, 406, 456, 506, 556]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    # missing from previous session end


    # auto-generated file download start  
    # auto-generated file download end


    # auto-generated file remove start 
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]