tasks = [
    # Generated on 2020-05-17 13:22:23.880000, contains telemetry from sessions 3439 to 3442.
    # The session starts on 2020-05-17 14:17:10+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(103, '/telemetry.previous', [1364, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1389]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1377, 1427, 1477]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1401, 1451, 1501, 1551]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1371, 1421, 1471, 1521, 1571, 1621]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1383, 1433, 1483, 1533, 1583, 1633, 1683]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/telemetry.previous', [1957, 2007, 2057, 2107, 2157, 2207, 2257]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 9, 59, 109, 159, 209, 259]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [309, 359, 409, 459, 509, 559, 609, 659, 709, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [597, 647, 697, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 41, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 3, 53, 103, 153, 203, 253, 303, 353]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.current', [403, 453, 503, 553, 603, 653, 703, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/telemetry.current', [665, 715, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(43, '/m9n_480_0', [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/m9w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/m4n_480_0', [24, 27, 28, 30, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/m4n_480_0', [45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/m4n_480_0', [62, 63, 64, 65, 67, 70, 71, 87, 89, 94, 95, 97, 98, 100, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/m4w_480_0', [20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 32, 34, 35, 36, 39, 40, 41, 43]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/m4w_480_0', [44, 49, 52, 53, 54, 56, 59, 61, 63, 64, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/m4w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/m4w_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/m5n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/m5n_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/m5n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/m5w_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/m5w_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/m5w_480_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/m5w_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/m6n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/m6n_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/m6n_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/m6w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/m6w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/m6w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/m6w_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/m6w_480_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/m6w_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/m6w_480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/m7n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/m7n_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/m7n_480_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/m7w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/m7w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/m7w_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/m7w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/m7w_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/m7w_480_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/m7w_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/m7w_480_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/m8n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/m8n_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/m8n_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/m8w_480_0', [7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/m8w_480_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/m8w_480_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/m8w_480_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/m8w_480_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/m8w_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/m8w_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/m8w_480_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/m8w_480_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/m9n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/m9n_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/m9n_480_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/m9n_480_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/m9w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/m9w_480_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/m9w_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/m9w_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/m9w_480_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/m9w_480_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/m9w_480_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]