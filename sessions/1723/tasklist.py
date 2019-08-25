tasks = [
    # Generated on 2019-08-26 00:32:01.847000, contains telemetry from sessions 1722 to 1723.
    # The session starts on 2019-08-26 10:12:29+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(84, '/telemetry.previous', [1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 1914, 1964, 2014, 2064]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 46, 96, 146, 196, 246]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.previous', [2114, 2164, 2214, 2264, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1920]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.current', [534, 584, 634, 684, 734, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 40, 90, 140, 190, 240]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.previous', [1970, 2020, 2070, 2120, 2170, 2220, 2270, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1944, 1994, 2044, 2094, 2144, 2194]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 2, 52, 102, 152, 202, 252, 302, 352, 402, 452]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [502, 552, 602, 652, 702, 752, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(33, '/telemetry.previous', [1720, 1733, 1739, 1745, 1770, 1777, 1783, 1795, 1820, 1827, 1883, 1895]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/t17n_480_0', [34, 49, 65, 85, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t14n_480_0', [16, 75, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t19n_480_0', [38, 57, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t15n_128_0', [23]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p12_128_0', [11]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t15w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t15w_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t19w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t19w_128_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t13n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t13n_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t13n_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t13n_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t13n_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t13n_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t13n_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t13w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t13w_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t14w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t14w_128_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t13n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t13n_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t17w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t17w_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t19n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t19n_128_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t12w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t12w_480_0', [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t12w_480_0', [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t14w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t14w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t14w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t14w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t14w_480_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t12w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t12w_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t14n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t12n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t16w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t16w_128_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t15n_480_0', [54, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t20w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t20n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t20w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 15, 16, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t20w_480_0', [46, 47, 48, 49, 51, 53, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t20w_480_0', [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t20w_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t20w_480_0', [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t20w_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t20n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t20n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t20n_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t20n_480_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]