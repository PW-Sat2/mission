tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Take photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(70, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(71, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(72, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(73, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(74, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(75, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(76, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(78, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(79, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is telemetry download.", Print, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2034, 2084, 2134, 2184, 2234, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [4, 54, 29, 17, 67, 41, 11, 61, 23, 35, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1071, 1121, 1171, 1221, 1271]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2041, 2091, 2141, 2191, 2241, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1077, 1127, 1177, 1227, 1277]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]