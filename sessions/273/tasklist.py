tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(60, '/p1_128_0', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_128_0', [i for i in range(12, 24, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p2_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p2_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p3_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p3_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p4_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p5_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [27, 77, 127, 177, 227, 52, 102, 152, 202, 40, 90, 140, 190, 240, 64, 114, 164, 214, 34, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [134, 184, 234, 46, 96, 146, 196, 246, 58, 108, 158, 208, 70, 120, 170, 220]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missings
    [tc.DownloadFile(30, '/telemetry.previous', [1041, 1053, 1065, 1077, 1091, 1103, 1115, 1127, 1141, 1153, 1165, 1177, 1191, 1203, 1215, 1227, 1241]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1253, 1265, 1277, 1291, 1303, 1315, 1327, 1341, 1353, 1365, 1377, 1391, 1403, 1415, 1427, 1441, 1453]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1465, 1477, 1491, 1503, 1515, 1527, 1541, 1553, 1565, 1577, 1591, 1603, 1615, 1627, 1641, 1653, 1665]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1677, 1691, 1703, 1715, 1727, 1741, 1753, 1765, 1777, 1791, 1803, 1815, 1827, 1841, 1853, 1865, 1877]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1891, 1903, 1915, 1927, 1941, 1953, 1965, 1977, 1991, 2003, 2015, 2027, 2041, 2053, 2065, 2077]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2091, 2103, 2115, 2127, 2141, 2153, 2165, 2177, 2191, 2203, 2215, 2227, 2241, 2253, 2265, 2277]), Send, WaitMode.Wait]
    #

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]