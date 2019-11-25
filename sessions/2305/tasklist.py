tasks = [
    # Generated on 2019-11-25 11:03:16.729000, contains telemetry from sessions 2304 to 2305.
    # The session starts on 2019-11-25 11:48:27+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [874, 881, 887, 893, 899, 905, 911, 917, 924, 931, 937, 943, 949, 955, 961, 967, 974, 981, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [993, 999, 1005, 1011, 1017, 1024, 1031, 1037, 1043, 1049, 1055, 1061, 1067, 1074, 1081, 1087, 1093, 1099, 1105]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1111, 1117, 1124, 1131, 1137, 1143, 1149, 1155, 1161, 1167, 1174, 1181, 1187, 1193, 1199, 1205, 1211, 1217]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1224, 1231, 1237, 1243, 1249, 1255, 1261, 1267, 1274, 1281, 1287, 1293, 1299, 1305, 1311, 1317, 1324, 1331]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1337, 1343, 1349, 1355, 1361, 1367, 1374, 1381, 1387, 1393, 1399, 1405, 1411, 1417, 1424, 1431, 1437, 1443]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1449, 1455, 1461, 1467, 1474, 1481, 1487, 1493, 1499, 1505, 1511, 1517, 1524, 1531, 1537, 1543, 1549, 1555]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1561, 1567, 1574, 1581, 1587, 1593, 1599, 1605, 1611, 1617, 1624, 1631, 1637, 1643, 1649, 1655, 1661, 1667]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1674, 1681, 1687, 1693, 1699, 1705, 1711, 1717, 1724, 1731, 1737, 1743, 1749, 1755, 1761, 1767, 1774, 1781]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1787, 1793, 1799, 1805, 1811, 1817, 1824, 1831, 1837, 1843, 1849, 1855, 1861, 1867, 1874, 1881, 1887, 1893]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1899, 1905, 1911, 1917, 1924, 1931, 1937, 1943, 1949, 1955, 1961, 1967, 1974, 1981, 1987, 1993, 1999, 2005]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t04n_240_17', [58, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t04n_240_18', [0, 1, 2, 3, 4, 6, 8, 9, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t04n_240_19', [10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t04n_240_20', [45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t04n_240_23', [0, 1, 4, 7, 16, 17, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t04n_240_23', [39, 40, 41, 42, 43, 44, 45, 46, 48, 49, 50, 52, 53, 54, 55, 56, 57, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t04n_240_24', [0, 1, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t04n_240_24', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 59, 60, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t04n_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t04n_240_25', [10, 11, 12, 13, 14, 15, 16, 51, 55, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t04n_240_26', [15, 36, 38, 45, 51, 52, 53, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t04n_240_27', [2, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t04n_240_27', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t04n_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t04n_240_28', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t04n_240_28', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated telemetry start
    [tc.DownloadFile(56, '/telemetry.previous', [2141, 2191, 2241, 2166, 2216, 2266, 2154, 2204, 2254, 2178, 2228, 2278, 2148, 2198, 2248, 2160, 2210, 2260, 2172, 2222]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [11, 61, 36, 24, 74, 48, 18, 68, 30, 80, 42, 4, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', [2272, 2184, 2234]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]