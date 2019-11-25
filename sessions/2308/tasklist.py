tasks = [
    # Generated on 2019-11-25 19:01:24.097242, contains telemetry from sessions 2306 to 2308.
    # The session starts on 2019-11-25 21:03:55+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059, 234, 284]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 222, 272, 322, 372]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 246, 296, 346, 396, 446, 496]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 216, 266, 316, 366, 416, 466, 516, 566, 616]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [666, 716, 766, 816, 866, 916, 966, 1016, 1066, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [778, 828, 878, 928, 978, 1028, 1078, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [890, 940, 990, 1040, 1090, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1002, 1052]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(40, '/t04n_240_25', [0, 7, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t04n_240_23', [26, 41, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t04n_240_24', [26, 45, 49, 52, 59, 60, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t04n_240_18', [8, 9, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t04n_240_19', [10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t04n_240_27', [2, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t04n_240_27', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t04n_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t04n_240_28', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t04n_240_28', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [874, 881, 887, 893, 899, 905, 911, 917, 924, 931, 937, 943, 949, 955, 961, 967, 974, 981, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [993, 999, 1005, 1011, 1017, 1024, 1031, 1037, 1043, 1049, 1055, 1061, 1067, 1074, 1081, 1087, 1093, 1099, 1105]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [1111, 1117, 1124, 1131, 1137, 1143, 1149, 1155, 1161, 1167, 1174, 1181, 1187, 1193, 1199, 1205, 1211, 1217]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [1224, 1231, 1237, 1243, 1249, 1255, 1261, 1267, 1274, 1281, 1287, 1293, 1299, 1305, 1311, 1317, 1324, 1331]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [1337, 1343, 1349, 1355, 1361, 1367, 1374, 1381, 1387, 1393, 1399, 1405, 1411, 1417, 1424, 1431, 1437, 1443]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [1449, 1455, 1461, 1467, 1474, 1481, 1487, 1493, 1499, 1505, 1511, 1517, 1524, 1531, 1537, 1543, 1549, 1555]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [1561, 1567, 1574, 1581, 1587, 1593, 1599, 1605, 1611, 1617, 1624, 1631, 1637, 1643, 1649, 1655, 1661, 1667]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [1674, 1681, 1687, 1693, 1699, 1705, 1711, 1717, 1724, 1731, 1737, 1743, 1749, 1755, 1761, 1767, 1774, 1781]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', [1787, 1793, 1799, 1805, 1811, 1817, 1824, 1831, 1837, 1843, 1849, 1855, 1861, 1867, 1874, 1881, 1887, 1893]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [1899, 1905, 1911, 1917, 1924, 1931, 1937, 1943, 1949, 1955, 1961, 1967, 1974, 1981, 1987, 1993, 1999, 2005]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [2011, 2017, 2023, 2029, 2035, 2041, 2047, 2053, 2059, 2065, 2071, 2077, 2083, 2089, 2095, 2101, 2107, 2113]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.previous', [2119, 2125, 2131, 2137]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
