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
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p1_240'), Send, WaitMode.Wait],    
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p2_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(16, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p3_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p4_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=16), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p5_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(24, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=16), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(26, CameraLocation.Nadir, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p6_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(28, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=48), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p7_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(30, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(31, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(32, CameraLocation.Nadir, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p8_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(33, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(34, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(35, CameraLocation.Wing, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p9_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(36, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(37, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(38, CameraLocation.Nadir, PhotoResolution.p240, 1, datetime.timedelta(minutes=0), 'p10_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(39, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],

    # =========================================

    # Low and mid res photos download

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/p1_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p1_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],


    [tc.ListFiles(104, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(105, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(106, '/p2_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p2_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],


    [tc.ListFiles(108, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(109, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p3_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p3_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],


    [tc.ListFiles(112, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(113, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(114, '/p4_240_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p4_240_0', [i for i in range(35, 70, 1)]), Send, WaitMode.Wait],


    [tc.ListFiles(116, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]