tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Start at 9:32 or ASAP (start over Poland)
    # Group 1
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
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
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(113, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(114, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(115, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(116, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(117, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(118, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(119, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(120, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(121, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],


    # ==============
    # Session routine moved here to take photos over Poland
    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 74 and 76 - few chunks to download. Should take less than a minute so it does not affect on photo queue.
    [tc.DownloadFile(3, '/telemetry.previous', [i for i in range(1650, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(0, 800, 100)]), Send, WaitMode.Wait],
    # ==============


    # Photo at 9:55 (start over South Africa)
    # Group 11
    [tc.TakePhotoTelecommand(122, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(123, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p11_480'), Send, WaitMode.Wait],

    # Group 12
    [tc.TakePhotoTelecommand(124, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p12_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(125, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p12_480'), Send, WaitMode.Wait],

    # Group 13
    [tc.TakePhotoTelecommand(126, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(127, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p13_480'), Send, WaitMode.Wait],

    # Group 14
    [tc.TakePhotoTelecommand(128, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p14_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(129, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p14_480'), Send, WaitMode.Wait],

    # Group 15
    [tc.TakePhotoTelecommand(130, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(131, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p15_480'), Send, WaitMode.Wait],

    # Group 16
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p16_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(133, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p16_480'), Send, WaitMode.Wait],

    # Group 17
    [tc.TakePhotoTelecommand(134, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p17_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(135, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p17_480'), Send, WaitMode.Wait],

    # Group 18
    [tc.TakePhotoTelecommand(136, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p18_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(137, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p18_480'), Send, WaitMode.Wait],

    # Group 19
    [tc.TakePhotoTelecommand(138, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p19_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(139, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p19_480'), Send, WaitMode.Wait],

    # Group 20
    [tc.TakePhotoTelecommand(140, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p20_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(141, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p20_480'), Send, WaitMode.Wait],


    # ==============
    # Set to 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    # ==============


    # More telemetry between session 74 and 76
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1616, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1632, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(16, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(32, 800, 50)]), Send, WaitMode.Wait],

    # Much more telemetry between session 74 and 76
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1608, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1624, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1640, 2280, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(8, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(24, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(40, 800, 50)]), Send, WaitMode.Wait],

    # Much much more telemetry between session 74 and 76
    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(1604, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.previous', [i for i in range(1612, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.previous', [i for i in range(1620, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.previous', [i for i in range(1628, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.previous', [i for i in range(1632, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.previous', [i for i in range(1644, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.previous', [i for i in range(1648, 2280, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(4, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [i for i in range(12, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.current', [i for i in range(20, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(28, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(32, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(44, 800, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
