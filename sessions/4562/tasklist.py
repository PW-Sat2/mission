tasks = [
    # Generated on 2020-11-08 10:06:56.352000, contains telemetry from sessions 4561 to 4562.
    # The session starts on 2020-11-08 11:14:22+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(72, '/telemetry.current', [168, 218, 268, 318, 368, 193, 243, 293, 343, 181, 231, 281, 331, 381, 205, 255, 305, 355, 175, 225]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [275, 325, 375, 187, 237, 287, 337, 199, 249, 299, 349, 211, 261, 311, 361]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [1, 7, 13, 19, 25, 32, 39, 45, 51, 57, 63, 69, 75, 82, 89, 95, 101]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [107, 113, 119, 125, 132, 139, 145, 151, 157, 163, 169, 175, 182, 189, 195, 201]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1362, 1369, 1375, 1381, 1393, 1399, 1405, 1412, 1419, 1425, 1431, 1437, 1443, 1449, 1455, 1462, 1469, 1475]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1481, 1487, 1493, 1499, 1505, 1512, 1519, 1525, 1531, 1537, 1543, 1549, 1555, 1562, 1569, 1575, 1581, 1587]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1593, 1599, 1605, 1612, 1619, 1625, 1631, 1637, 1643, 1649, 1655, 1662, 1669, 1675, 1681, 1687, 1693, 1699]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1705, 1712, 1719, 1725, 1731, 1737, 1743, 1749, 1755, 1762, 1769, 1775, 1781, 1787, 1793, 1799, 1805, 1812]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1819, 1825, 1831, 1837, 1843, 1849, 1855, 1862, 1869, 1875, 1881, 1887, 1893, 1899, 1905, 1919, 1925, 1931]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1937, 1943, 1949, 1955, 1969, 1975, 1981, 1987, 1993, 1999, 2005, 2019, 2025, 2031, 2037, 2043, 2049]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2055, 2069, 2075, 2081, 2087, 2093, 2099, 2105, 2112, 2119, 2125, 2131, 2137, 2143, 2149, 2155, 2162]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2169, 2175, 2181, 2187, 2193, 2199, 2205, 2212, 2219, 2225, 2231, 2237, 2243, 2249, 2255, 2269, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/n_w_1_0', [157]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/n_w_2_0', [19, 38, 39, 40, 41, 48, 49, 50, 51, 52, 53, 57, 58, 59, 60, 61, 62, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/n_w_2_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/n_w_3_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/n_w_3_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/n_w_3_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/n_w_3_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/n_w_4_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/n_w_4_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/n_w_4_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/n_w_4_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/n_w_5_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/n_w_5_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/n_w_5_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/n_w_5_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/n_w_6_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/n_w_6_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/n_w_6_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/n_w_6_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/n_w_6_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/n_w_6_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/n_w_6_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/n_w_6_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/n_w_7_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/n_w_7_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/n_w_7_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/n_w_7_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/n_w_8_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/n_w_8_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/n_w_8_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/n_w_8_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/n_w_8_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]