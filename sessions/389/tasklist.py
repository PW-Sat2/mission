tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1591, 1641, 1691, 1741, 1791]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [36, 86, 136, 186, 236, 286, 336, 11, 61, 111, 161, 211, 261, 311, 49, 99, 149, 199, 249, 299]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2129, 2179, 2229, 2279, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1573, 1623]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [349, 23, 73, 123, 173, 223, 273, 323, 43, 93, 143, 193, 243, 293, 343, 5, 55, 105, 155, 205]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 1585, 1635, 1685, 1735, 1785, 1835, 1885]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1935, 1985, 2035, 2085, 2135, 2185, 2235, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [255, 305, 17, 67, 117, 167, 217, 267, 317, 29, 79, 129, 179, 229, 279, 329]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2247, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(62, '/p2_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p2_128_0', [i for i in range(18, 22, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p3_128_0', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/p4_128_0', [i for i in range(0, 13, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(68, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p5_128_0', [i for i in range(18, 21, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/p6_128_0', [i for i in range(0, 14, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(72, '/p7_128_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/p8_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p8_128_0', [i for i in range(18, 21, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/p9_128_0', [i for i in range(0, 14, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(78, '/p10_128_0', [i for i in range(0, 13, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]