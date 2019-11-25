tasks = [
    # Generated on 2019-11-25 13:01:49.501649, contains telemetry from sessions 2304 to 2307.
    # The session starts on 2019-11-25 19:31:45+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [2141, 2191, 2241, 2166, 2216, 2266, 2154, 2204, 2254, 2178, 2228, 2278, 2148, 2198, 2248, 2160, 2210, 2260, 2172, 2222]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [11, 61, 111, 161, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 24, 74, 124]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [174, 224, 274, 324, 374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 48, 98, 148, 198]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 18, 68, 118, 168, 218, 268]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 30, 80, 130, 180, 230, 280, 330]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 42, 92, 142, 192, 242, 292, 342, 392, 442]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2272, 2184, 2234]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [492, 542, 592, 642, 692, 742, 792, 842, 892, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [554, 604, 654, 704, 754, 804, 854, 904]), Send, WaitMode.Wait],
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