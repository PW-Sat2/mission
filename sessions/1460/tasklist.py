tasks = [
    # Generated on 2019-06-28 22:47:34.288000.
    # The session starts on 2019-06-29 11:17:49+02:00.


    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p0w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p0n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(21, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(22, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(26, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(30, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p10_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(31, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(32, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p12_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(33, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(34, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p14_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(35, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(36, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p16_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(37, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p17_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(38, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p18_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(39, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p19_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(40, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p20_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(41, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p21_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(42, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p22_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p23_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(44, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p24_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(45, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p25_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(46, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p26_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(47, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p27_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(48, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p28_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(49, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p29_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(50, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p20_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(51, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p31_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(52, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p32_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(53, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p33_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(54, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p34_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(55, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p35_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(56, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p36_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(57, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p37_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(58, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p38_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(59, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p39_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(60, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p30_128'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(61, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p41_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(62, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p42_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(63, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p43_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(64, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p44_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(65, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p45_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(66, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p46_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(67, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p47_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(68, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p48_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(69, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p49_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(70, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=10), 'p50_128'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(80, CameraLocation.Wing, PhotoResolution.p128, 50, datetime.timedelta(minutes=80), 'p51_128'), Send, WaitMode.Wait],

    # =========================================

    # Low and mid res photos download

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(201, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(202, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(203, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p15_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(204, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p20_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(205, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p25_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(206, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p30_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(207, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p35_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(208, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p40_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(209, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p45_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(210, '/'), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p50_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.ListFiles(211, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]