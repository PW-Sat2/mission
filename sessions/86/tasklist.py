tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],


    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 85 and 86
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(2030, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(2036, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(2033, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(2039, 2230, 12)]), Send, WaitMode.Wait],

    # Wait until 21:37 on SendBeacon telecommand
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Start at 21:37
    # Group 1
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=14), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(104, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(105, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(106, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(109, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(110, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(111, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(113, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(114, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(115, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(116, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(117, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(118, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(119, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(120, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(121, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],

    # Group 11
    [tc.TakePhotoTelecommand(122, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(123, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p11_480'), Send, WaitMode.Wait],

    # Group 12
    [tc.TakePhotoTelecommand(124, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p12_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(125, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p12_480'), Send, WaitMode.Wait],

    # Group 13
    [tc.TakePhotoTelecommand(126, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(127, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p13_480'), Send, WaitMode.Wait],

    # Group 14
    [tc.TakePhotoTelecommand(128, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p14_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(129, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p14_480'), Send, WaitMode.Wait],

    # Group 15
    [tc.TakePhotoTelecommand(130, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(131, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p15_480'), Send, WaitMode.Wait],

    # Group 16
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p16_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(133, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p16_480'), Send, WaitMode.Wait],

    # Group 17
    [tc.TakePhotoTelecommand(134, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p17_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(135, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p17_480'), Send, WaitMode.Wait],

    # Group 18
    [tc.TakePhotoTelecommand(136, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p18_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(137, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p18_480'), Send, WaitMode.Wait],

    # Group 19
    [tc.TakePhotoTelecommand(138, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p19_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(139, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p19_480'), Send, WaitMode.Wait],

    # Group 20
    [tc.TakePhotoTelecommand(140, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p20_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(141, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p20_480'), Send, WaitMode.Wait],

    # Second bunch of photos over Antarctica
    [tc.TakePhotoTelecommand(142, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=20), 'p21_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(143, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=3), 'p22_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(144, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=3), 'p23_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(145, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=3), 'p24_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(146, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=3), 'p25_128'), Send, WaitMode.Wait],


    # More telemetry between session 85 and 86
    [tc.DownloadFile(200, '/telemetry.current', [i for i in range(2031, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [i for i in range(2032, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [i for i in range(2034, 2230, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(203, '/telemetry.current', [i for i in range(2035, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/telemetry.current', [i for i in range(2037, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/telemetry.current', [i for i in range(2038, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/telemetry.current', [i for i in range(2040, 2230, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(207, '/telemetry.current', [i for i in range(2041, 2230, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 84 and 85
    [tc.DownloadFile(208, '/telemetry.current', [i for i in range(1351, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(209, '/telemetry.current', [i for i in range(1352, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(210, '/telemetry.current', [i for i in range(1354, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(211, '/telemetry.current', [i for i in range(1355, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(212, '/telemetry.current', [i for i in range(1357, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(213, '/telemetry.current', [i for i in range(1358, 2200, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(214, '/telemetry.current', [i for i in range(1360, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(215, '/telemetry.current', [i for i in range(1361, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(216, '/telemetry.current', [i for i in range(1363, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(217, '/telemetry.current', [i for i in range(1364, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(218, '/telemetry.current', [i for i in range(1366, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(219, '/telemetry.current', [i for i in range(1367, 2200, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(220, '/telemetry.current', [i for i in range(1369, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(221, '/telemetry.current', [i for i in range(1370, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(222, '/telemetry.current', [i for i in range(1372, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(223, '/telemetry.current', [i for i in range(1373, 2200, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
