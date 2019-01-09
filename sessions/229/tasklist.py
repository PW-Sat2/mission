tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Take photo queue
    # Group 1 - Poland (10:17)
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(70, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(71, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(72, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(73, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3 - South Pole
    [tc.TakePhotoTelecommand(74, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=30), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(75, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4 - New Zeland
    [tc.TakePhotoTelecommand(76, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=20), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5 - Sea of Okhotsk
    [tc.TakePhotoTelecommand(78, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=23), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(79, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.ListFiles(99, '/'), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [[tc.DownloadFile(correlation_id=201, path='/p2_128_0', seqs=range(0, 22)), Send, WaitMode.Wait]]
    [[tc.DownloadFile(correlation_id=202, path='/p1_128_0', seqs=range(0, 25)), Send, WaitMode.Wait]]

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]