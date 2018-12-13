tasks = [
    [[tc.SetBitrate(50, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(51, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(750, 1900, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(790, 1900, 100)]), Send, WaitMode.Wait],

    [tc.SetBitrate(93, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Sent telecommand at T=9:20 
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Photo at 9:40 (start over South Africa)
    # Group 1
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=20), 'p1_128'), Send, WaitMode.Wait],
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

    # Beacon
    [tc.SendBeacon(), Send, WaitMode.Wait],    

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


    # Telemetry over night    
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(770, 1900, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(810, 1900, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(760, 1900, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(780, 1900, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(800, 1900, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]

# 900 frames @ 9600 - 154.7mWh
