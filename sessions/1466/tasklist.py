tasks = [
    # Generated on 2019-07-14 10:15:37.924000, contains telemetry from sessions 1465 to 1466.
    # The session starts on 2019-07-14 11:32:01+02:00.

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

    # auto-generated telemetry start
    [tc.DownloadFile(74, '/telemetry.current', [197, 247, 297, 347, 397, 222, 272, 322, 372, 210, 260, 310, 360, 410, 234, 284, 334, 384, 204, 254]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [304, 354, 404, 216, 266, 316, 366, 416, 228, 278, 328, 378, 240, 290, 340, 390]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p52_128_13', [35]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p52_128_12', [4, 5, 6, 19, 20, 25, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p52_128_11', [0, 16, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p52_128_17', [13, 14, 15, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [2, 9, 15, 21, 27, 33, 39, 45, 52, 59, 65, 71, 77, 83, 89, 95, 102, 109, 115]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [121, 127, 133, 139, 145, 152, 159, 165, 171, 177, 183, 189, 195, 202, 209, 215, 221, 227, 233]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p52_128_15', [21, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p52_128_14', [0, 3, 4, 7, 8, 9, 12, 13, 14, 15, 16, 17, 22, 27, 31, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p52_128_19', [0, 4, 6, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p52_128_19', [20, 21, 22, 23, 24, 25, 27, 29, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p52_128_18', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p52_128_18', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p52_128_26', [0, 1, 2, 3, 4, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p52_128_26', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p47_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1225, 1263, 1275, 1300, 1325, 1350, 1375, 1382, 1389, 1395, 1401, 1407, 1413, 1419, 1425, 1432, 1439, 1445, 1451]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1457, 1463, 1469, 1475, 1482, 1489, 1495, 1501, 1507, 1513, 1519, 1525, 1532, 1539, 1545, 1551, 1557, 1563, 1569]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1575, 1582, 1589, 1595, 1601, 1607, 1613, 1619, 1625, 1632, 1639, 1645, 1651, 1657, 1663, 1669, 1675, 1682, 1689]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1695, 1701, 1707, 1713, 1719, 1725, 1732, 1739, 1745, 1751, 1757, 1763, 1769, 1775, 1782, 1789, 1795, 1801, 1807]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1813, 1819, 1825, 1832, 1839, 1845, 1851, 1857, 1863, 1869, 1875, 1882, 1889, 1895, 1901, 1907, 1913, 1919, 1925]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1932, 1939, 1945, 1951, 1957, 1963, 1969, 1975, 1982, 1989, 1995, 2001, 2007, 2013, 2019, 2025, 2032, 2039, 2045]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [2051, 2057, 2063, 2069, 2075, 2082, 2089, 2095, 2101, 2107, 2113, 2119, 2125, 2132, 2139, 2145, 2151, 2157, 2163]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [2169, 2175, 2182, 2189, 2195, 2201, 2207, 2213, 2219, 2225, 2232, 2239, 2245, 2251, 2257, 2263, 2269, 2275]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p25_128_0', [18, 19, 20, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p27_128_0', [0, 3, 4, 6, 7, 8, 11, 12, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p24_128_0', [14, 15, 17, 19, 20, 22, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p21_128_0', [15, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_9', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_9', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_9', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_9', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_9', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_9', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_9', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_9', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_9', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/suns_ps_9', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/suns_ps_9', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/suns_ps_9', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p41_128_0', [4, 5]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p20_128_0', [25]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p52_128_16', [16, 17, 19, 21, 22, 23, 25, 29, 30, 31, 35]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]