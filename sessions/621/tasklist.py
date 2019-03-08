tasks = [
    # Generated on 2019-03-08 23:30:52.074000, contains telemetry from sessions 618 to 621.
    # The session starts on 2019-03-09 10:15:13+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],
    
    # =========================================

    ["The next step is telemetry download.", Print, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [26, 76, 1, 51, 101, 39, 89, 13, 63, 113, 33, 83, 45, 95, 7, 57, 107, 19, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 919, 969, 1019, 1069, 1119]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2169, 2219, 2269, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 925, 975]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2025, 2075, 2125, 2175, 2225, 2275, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 949, 999, 1049, 1099, 1149, 1199, 1249]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]