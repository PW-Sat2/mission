tasks = [
    # Generated on 2019-08-11 07:45:30.199392, contains telemetry from sessions 1632 to 1633.
    # The session starts on 2019-08-11 10:11:39+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(10, '/telemetry.previous', [1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1585, 1635, 1685, 1735, 1785]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [30, 80, 130, 180, 230, 280, 330, 380, 5, 55, 105, 155, 205, 255, 305, 355, 405, 43, 93, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [2123, 2173, 2223, 2273, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1567, 1617]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [193, 243, 293, 343, 393, 17, 67, 117, 167, 217, 267, 317, 367, 37, 87, 137, 187, 237, 287, 337]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267, 1579, 1629, 1679, 1729, 1779, 1829, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [387, 49, 99, 149, 199, 249, 299, 349, 399, 11, 61, 111, 161, 211, 261, 311, 361, 411, 23, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.previous', [1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.previous', [2191, 2241, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [123, 173, 223, 273, 323, 373]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p12_128_0', [16]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [743, 793, 943, 1043, 1081, 1093, 1131, 1143, 1181, 1219, 1269, 1293, 1319, 1369, 1459, 1528, 1578]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p12_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p12_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p12_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p12_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p12_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p12_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p12_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p12_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p12_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p11_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p11_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p11_480_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p11_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p4_480_0', [53, 59, 63, 69, 70, 78, 79, 80, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p4_480_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p11_128_0', [2, 3, 4, 6, 7, 8, 9, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p13_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p13_480_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p9_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p9_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p9_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p9_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p9_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p9_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p9_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p9_480_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]), Send, WaitMode.Wait]
    [tc.DownloadFile(58, '/p5_480_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p6_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p6_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p6_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]