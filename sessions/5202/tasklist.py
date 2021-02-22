tasks = [
    # Generated on 2021-02-22 14:01:01.960691, contains telemetry from sessions 5200 to 5202.
    # The session starts on 2021-02-22 21:17:27+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(41, '/telemetry.previous', [2028, 2160]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [729, 82, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1886, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1861, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1849, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1873, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1843, 905, 955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1855, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1867, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(42, '/pw_p10_0', [28, 29, 30, 39, 52, 53, 54, 55, 56, 57, 58, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(77, 'n01n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(78, 'n01w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(79, 'n02n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(80, 'n02w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(81, 'p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(82, 'p1_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(83, 'p1_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(84, 'p1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(85, 'p2_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(86, 'p2_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(87, 'p5174_0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(88, 'p5174_1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(89, 'radfet_60'), Send, WaitMode.Wait],
    [tc.RemoveFile(90, 'radfet_61'), Send, WaitMode.Wait],
    [tc.ListFiles(91, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
