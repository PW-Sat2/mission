tasks = [
    # Generated on 2021-02-22 21:32:36.544367, contains telemetry from sessions 5200 to 5203.
    # The session starts on 2021-02-22 22:43:33+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.SetPeriodicMessageTelecommand(100, interval_minutes=3, repeat_count=1, message='Goodbye PW-Sat2 and youtu.be/dQw4w9WgXcQ'), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(149, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=17), 'o1_w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(150, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'o1_w_128'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(151, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'o1_n_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(152, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'o1_n_480'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(51, '/telemetry.current', [886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1886, 1936, 1986, 2036, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1711, 1761, 1811, 1861, 1911, 1961, 2011, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 893, 943, 993, 1043, 1093, 1143, 1193]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 905, 955, 1005]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [1917, 1967, 2017, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [1779, 1829, 1879, 1929, 1979, 2029]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [82, 729, 886, 893, 899, 905, 911, 917, 923, 929, 936, 943, 949, 955, 961, 967, 973, 979, 986]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [993, 999, 1005, 1011, 1017, 1023, 1029, 1036, 1043, 1049, 1055, 1061, 1067, 1073, 1079, 1086, 1093, 1099]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1105, 1111, 1117, 1123, 1129, 1136, 1143, 1149, 1155, 1161, 1167, 1173, 1179, 1186, 1193, 1199, 1205, 1211]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1217, 1223, 1229, 1236, 1243, 1249, 1255, 1261, 1267, 1273, 1279, 1286, 1293, 1299, 1305, 1311, 1317, 1323]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1329, 1336, 1343, 1349, 1355, 1361, 1367, 1373, 1379, 1386, 1393, 1399, 1405, 1411, 1417, 1423, 1429, 1436]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1443, 1449, 1455, 1461, 1467, 1473, 1479, 1486, 1493, 1499, 1505, 1511, 1517, 1523, 1529, 1536, 1543, 1549]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1555, 1561, 1567, 1573, 1579, 1586, 1593, 1599, 1605, 1611, 1617, 1623, 1629, 1636, 1643, 1649, 1655, 1661]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1667, 1673, 1679, 1686, 1693, 1699, 1705, 1711, 1717, 1723, 1729, 1736, 1743, 1749, 1755, 1761, 1767, 1773]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1779, 1786, 1793, 1799, 1805, 1811, 1817, 1823, 1829, 1836, 1843, 1849, 1855, 1861, 1867, 1873, 1879, 1886]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2028, 2160]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/pw_p10_0', [28, 29, 30, 39, 52, 53, 54, 55, 56, 57, 58, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]