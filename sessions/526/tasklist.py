tasks = [
    # Generated on 2019-02-23 09:35:35.155995, contains telemetry from sessions 522 to 526.
    # The session starts on 2019-02-23 10:49:06+01:00.

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
    [tc.DownloadFile(30, '/telemetry.current', [460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 485, 535, 585, 635, 685, 735]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1785, 1835, 1885, 1935, 1985, 2035, 2085, 473, 523, 573, 623, 673, 723, 773, 823, 873, 923, 973, 1023, 1073]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 467, 517, 567, 617, 667, 717, 767]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1817, 1867, 1917, 1967, 2017, 2067, 2117, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 503, 553, 603, 653, 703, 753, 803]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1853, 1903, 1953, 2003, 2053, 2103]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]