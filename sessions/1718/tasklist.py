tasks = [
     [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(78, '/telemetry.current', [366, 416, 466, 516, 566, 391, 441, 491, 541, 379, 429, 479, 529, 579, 403, 453, 503, 553, 373, 423]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [473, 523, 573, 385, 435, 485, 535, 585, 397, 447, 497, 547, 409, 459, 509, 559]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing, part 1
    [tc.DownloadFile(55, '/telemetry.previous', [1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', [1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [1450, 1451, 1452, 1453, 1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.previous', [1477, 1561, 1573, 1585, 1591, 1597, 1611, 1623, 1635, 1641, 1647, 1661, 1673, 1685, 1691, 1697, 1711, 1723, 1735, 1741]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [1747, 1761, 1773, 1785, 1791, 1797, 1811, 1823, 1835, 1841, 1847, 1861, 1873, 1885, 1891, 1897, 1911, 1923, 1935, 1941]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [1947, 1961, 1973, 1985, 1991, 1997, 2011, 2023, 2035, 2041, 2047, 2061, 2067, 2073, 2085, 2091, 2097, 2111, 2117]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [2123, 2135, 2141, 2147, 2161, 2167, 2173, 2185, 2191, 2197, 2211, 2217, 2223, 2235, 2241, 2247, 2261, 2267, 2273]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [5, 11, 17, 31, 43, 55, 61, 67, 81, 93, 105, 111, 117, 131, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [155, 161, 167, 181, 193, 205, 211, 217, 231, 237, 243, 255, 261, 267, 281]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [287, 293, 305, 311, 317, 331, 337, 343, 355, 361, 367, 381, 387, 393, 405]), Send, WaitMode.Wait],
    # end missing

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Super Long Photos Part 2 - aim into 11:52

    # Orbit 8, 11:57, 40 N, Italy
    [tc.TakePhotoTelecommand(200, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=5), 't12w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(201, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12w_480'), Send, WaitMode.NoWait],
    [tc.TakePhotoTelecommand(202, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't12n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(203, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12n_480'), Send, WaitMode.Wait],

    # Orbit 8, time extender
    [tc.TakePhotoTelecommand(204, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_7'), Send, WaitMode.Wait],
 
    # Orbit 9, 13:29, 50 N, UK
    [tc.TakePhotoTelecommand(205, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=32), 't13w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(206, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(207, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't13n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(208, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13n_480'), Send, WaitMode.Wait],

    # Orbit 9, 13:33, 40 N, Portugal
    [tc.TakePhotoTelecommand(209, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 't14w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(210, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(211, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't14n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14n_480'), Send, WaitMode.Wait],

    # Orbit 9, time extender
    [tc.TakePhotoTelecommand(213, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_8'), Send, WaitMode.Wait],
 
    # Orbit 10, 15:02, 60 N, Island
    [tc.TakePhotoTelecommand(214, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't15w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(215, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(216, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't15n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(217, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15n_480'), Send, WaitMode.Wait],

    # Orbit 10, 15:09, 40 N, ocean
    [tc.TakePhotoTelecommand(218, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't16w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(219, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't16n_128'), Send, WaitMode.Wait], 
 
    # Orbit 10, time extender
    [tc.TakePhotoTelecommand(220, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_9'), Send, WaitMode.Wait],
 
    # Orbit 11, 16:36, 60 N, Greenland
    [tc.TakePhotoTelecommand(221, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=27), 't17w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(222, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't17w_480'), Send, WaitMode.NoWait],
    [tc.TakePhotoTelecommand(223, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't17n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(224, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't17n_480'), Send, WaitMode.Wait],

    # Orbit 11, 16:45, 40 N, ocean
    [tc.TakePhotoTelecommand(225, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=9), 't18w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(226, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't18n_128'), Send, WaitMode.Wait], 
 
    # Orbit 11, time extender
    [tc.TakePhotoTelecommand(227, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_10'), Send, WaitMode.Wait],
 
    # Orbit 12, 18:21, 40 N, USA East
    [tc.TakePhotoTelecommand(228, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't19w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(229, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't19w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(230, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't19n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(231, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't19n_480'), Send, WaitMode.Wait],

    # Orbit 12, time extender
    [tc.TakePhotoTelecommand(232, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_11'), Send, WaitMode.Wait],
 
    # Orbit 13, 19:57, 40 N, USA West
    [tc.TakePhotoTelecommand(233, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't20w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(234, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't20w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(235, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't20n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(236, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't20n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start

    [tc.DownloadFile(45, '/p1_128_0', [11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p2_128_0', [3, 5, 6, 14, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p4_128_0', [6, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p5_128_0', [24]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p17_128_0', [4, 5, 11, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p16_128_0', [3, 4, 5, 6]), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p15_128_0', [0, 1, 3, 5, 6, 9, 11, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p11_128_0', [0, 1, 2, 4, 5, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],

    [tc.DownloadFile(49, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],

    [tc.DownloadFile(43, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],   
    [tc.DownloadFile(39, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # missing from previous session end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]