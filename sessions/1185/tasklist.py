tasks = [
    # Generated on 2019-06-02 00:54:43.243000, contains telemetry from sessions 1183 to 1185.
    # The session starts on 2019-06-02 10:41:05+02:00.

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

    # sixth post-sail SunS experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_6'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1411, 1461]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [6, 56, 106, 156, 206, 256, 306, 356, 406, 31, 81, 131, 181, 231, 281, 331, 381, 19, 69, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1399, 1449, 1499, 1549]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 1423, 1473, 1523, 1573, 1623, 1673]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [169, 219, 269, 319, 369, 43, 93, 143, 193, 243, 293, 343, 393, 13, 63, 113, 163, 213, 263, 313]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [363, 413, 25, 75, 125, 175, 225, 275, 325, 375, 37, 87, 137, 187, 237, 287, 337, 387, 49, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2017, 2067, 2117, 2167, 2217, 2267, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2129, 2179, 2229, 2279]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [149, 199, 249, 299, 349, 399]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    [tc.DownloadFile(42, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p10_128_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p10_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p10_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p10_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p10_480_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p10_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]