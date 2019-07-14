tasks = [
    # Generated on 2019-07-14 00:26:48.505000, contains telemetry from sessions 1464 to 1465.
    # The session starts on 2019-07-14 09:57:38+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(65, '/telemetry.previous', [1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1407, 1457]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [2, 52, 102, 152, 202, 27, 77, 127, 177, 227, 15, 65, 115, 165, 215, 39, 89, 139, 189, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.previous', [1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1395, 1445, 1495, 1545]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.previous', [1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1419, 1469, 1519, 1569, 1619, 1669]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.previous', [1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.previous', [1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [59, 109, 159, 209, 21, 71, 121, 171, 221, 33, 83, 133, 183, 233, 45, 95, 145, 195]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.previous', [1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.previous', [2013, 2063, 2113, 2163, 2213, 2263, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.previous', [2125, 2175, 2225, 2275]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p52_128_13', [35]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p52_128_12', [4, 5, 6, 19, 20, 25, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p52_128_11', [0, 16, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p52_128_17', [13, 14, 15, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1225, 1263, 1275, 1300, 1325, 1350, 1375, 1425]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p52_128_15', [21, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p52_128_14', [0, 3, 4, 7, 8, 9, 12, 13, 14, 15, 16, 17, 22, 27, 31, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p52_128_19', [0, 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p52_128_19', [20, 21, 22, 23, 24, 25, 27, 29, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p52_128_18', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p52_128_18', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p52_128_26', [0, 1, 2, 3, 4, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p52_128_26', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p47_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p25_128_0', [18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p27_128_0', [0, 3, 4, 6, 7, 8, 11, 12, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p24_128_0', [14, 15, 17, 19, 20, 22, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p21_128_0', [15, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_9', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_9', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_9', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_9', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_9', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_9', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_9', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_9', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_9', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_9', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_9', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_9', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p41_128_0', [4, 5]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p20_128_0', [25]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p52_128_16', [16, 17, 19, 21, 22, 23, 25, 29, 30, 31, 35]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]