tasks = [
    # Generated on 2021-02-20 11:10:27.570000, contains telemetry from sessions 5187 to 5188.
    # The session starts on 2021-02-20 12:04:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(52, '/telemetry.previous', [2259, 2272, 2266, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [29, 79, 129, 179, 4, 54, 104, 154, 42, 92, 142, 16, 66, 116, 166, 36, 86, 136, 186, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [98, 148, 10, 60, 110, 160, 22, 72, 122, 172]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(10, '/radfet_61', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/telemetry.current', [1, 7, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1069, 1075, 1107, 1113, 1119, 1125, 1157, 1163, 1169, 1175, 1207, 1219, 1225, 1237, 1250, 1257, 1269, 1275]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1287, 1300, 1307, 1319, 1325, 1369, 1375, 1387, 1393, 1407, 1419, 1425, 1437, 1457, 1469, 1475, 1481, 1519]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1525, 1531, 1569, 1575, 1593, 1619, 1625, 1643, 1663, 1669, 1675, 1681, 1687, 1693, 1713, 1719, 1725, 1731]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1737, 1743, 1769, 1775, 1781, 1787, 1819, 1825, 1831, 1837, 1850, 1869, 1875, 1881, 1887, 1900, 1919, 1931]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1937, 1943, 1950, 1969, 1987, 1993, 2000, 2007, 2037, 2043, 2050, 2057, 2075, 2087, 2093, 2100, 2107]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2119, 2125, 2137, 2143, 2150, 2157, 2163, 2169, 2193, 2200, 2207, 2213, 2243, 2250, 2257, 2263, 2269]), Send, WaitMode.Wait],


    [tc.DownloadFile(37, '/p1_n_480_0', [0, 19, 25, 27, 29, 30, 31, 32, 33, 34, 39, 41, 56, 57, 59, 60, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p1_n_480_0', [65, 80, 81, 93, 94, 95, 96, 98, 99, 100, 106, 107, 108, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p1_n_480_0', [114, 118, 119, 120, 121, 127, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p1_n_480_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_w_480_0', [60, 61, 63, 64, 80, 81, 95, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p1_w_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p1_w_480_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],


    # 12:08 - start of the queue
    # orbit 1
    # 12:13 - first photo
    # 12:43 - last photo
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=5), 'pw_p0'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p3'), Send, WaitMode.Wait],

    # orbit 2
    # 13:33 - first photo
    # 14:13 - last photo
    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=50), 'pw_p4'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p5'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p6'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(108, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p8'), Send, WaitMode.Wait],

    # orbit 3
    # 15:03 - first photo
    # 15:43 - last photo
    [tc.TakePhotoTelecommand(109, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=50), 'pw_p9'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(110, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p10'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(111, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p11'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(112, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p12'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(113, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p13'), Send, WaitMode.Wait],

    # orbit 4
    # 16:38 - first photo
    # 17:18 - last photo
    [tc.TakePhotoTelecommand(114, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=55), 'pw_p14'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(115, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p15'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(116, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p16'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(117, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p17'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(118, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p18'), Send, WaitMode.Wait],

    # orbit 5
    # 18:08 - first photo
    # 18:48 - last photo
    [tc.TakePhotoTelecommand(119, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=50), 'pw_p19'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(120, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p20'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(121, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p21'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(122, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p22'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(123, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p23'), Send, WaitMode.Wait],

    # orbit 6
    # 19:38 - first photo
    # 20:18 - last photo
    [tc.TakePhotoTelecommand(124, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=50), 'pw_p24'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(125, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p25'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(126, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p26'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(127, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p27'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(128, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=10), 'pw_p28'), Send, WaitMode.Wait],


    # missing from previous session start
    [tc.DownloadFile(44, '/p2_n_480_0', [82, 83, 84, 85, 86, 87, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p2_n_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p2_n_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p2_n_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p2_w_480_0', [4, 10, 39, 40, 41, 43, 80, 81, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p2_w_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p2_w_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p2_w_480_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]