tasks = [
    # Generated on 2021-02-23 00:24:41.406000, contains telemetry from sessions 5204 to 5205.
    # The session starts on 2021-02-23 11:00:16+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(149, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=17), 'o1_w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(150, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'o1_n_128'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(151, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'o1_w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(152, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'o1_n_480'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(66, '/telemetry.previous', [2161, 2211, 2261, 2186, 2236, 2174, 2224, 2274, 2198, 2248, 2168, 2218, 2268, 2180, 2230, 2192, 2242, 2204, 2254]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [31, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [1031, 1081, 6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [906, 956, 1006, 1056, 1106, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [794, 844, 894, 944, 994, 1044, 1094, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [668, 718, 768, 818, 868, 918, 968, 1018, 1068, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 0, 50, 100, 150, 200, 250, 300, 350, 400]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 12, 62, 112, 162, 212, 262]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062, 24, 74, 124, 174]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [224, 274, 324, 374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.previous', [82, 729, 893, 905, 917, 929, 943, 949, 955, 967, 979, 993, 1005, 1017, 1029, 1055, 1067, 1079, 1105]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1117, 1129, 1155, 1167, 1179, 1205, 1217, 1229, 1243, 1255, 1267, 1279, 1293, 1305, 1317, 1329, 1343, 1355, 1367]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1379, 1393, 1405, 1417, 1423, 1429, 1443, 1455, 1467, 1479, 1493, 1505, 1517, 1529, 1543, 1555, 1567, 1573, 1579]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1593, 1605, 1617, 1623, 1629, 1643, 1655, 1667, 1679, 1693, 1705, 1717, 1729, 1743, 1755, 1767, 1779, 1793, 1805]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1817, 1829, 1843, 1855, 1867, 1879, 1893, 1905, 1917, 1929, 1943, 1955, 1967, 1979, 1993, 2001, 2005, 2008, 2014]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2017, 2020, 2023, 2026, 2029, 2032, 2038, 2043, 2044, 2051, 2058, 2064, 2070, 2076, 2082, 2088, 2094, 2101]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2108, 2114, 2120, 2126, 2132, 2138, 2144, 2151, 2158, 2164, 2170, 2176, 2182, 2188, 2194, 2201, 2208, 2214]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2028, 2160]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/pw_p10_0', [28, 29, 30, 39, 52, 53, 54, 55, 56, 57, 58, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]