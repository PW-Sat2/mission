tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(3, '/telemetry.previous', [i for i in range(1100, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.previous', [i for i in range(1150, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(0, 50, 10)]), Send, WaitMode.Wait],

    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Remove not removed files
    [tc.RemoveFile(7, '/p8_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(8, '/suns_2_sec'), Send, WaitMode.Wait],

    # Sent telecommand at T=9:23 
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Photo at 9:40 (start over South Africa)
    # Group 1
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=17), 'p1_128'), Send, WaitMode.Wait],
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
    [tc.DownloadFile(200, '/telemetry.previous', [i for i in range(1108, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.previous', [i for i in range(1116, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.previous', [i for i in range(1132, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.previous', [i for i in range(1140, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Much more telemetry
    [tc.DownloadFile(210, '/telemetry.previous', [i for i in range(1104, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(211, '/telemetry.previous', [i for i in range(1120, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(212, '/telemetry.previous', [i for i in range(1128, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(213, '/telemetry.previous', [i for i in range(1136, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(214, '/telemetry.previous', [i for i in range(1144, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Much much more telemetry
    [tc.DownloadFile(215, '/telemetry.previous', [i for i in range(1101, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(216, '/telemetry.previous', [i for i in range(1102, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(217, '/telemetry.previous', [i for i in range(1103, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(218, '/telemetry.previous', [i for i in range(1105, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(219, '/telemetry.previous', [i for i in range(1106, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(220, '/telemetry.previous', [i for i in range(1107, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(221, '/telemetry.previous', [i for i in range(1109, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(222, '/telemetry.previous', [i for i in range(1110, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(223, '/telemetry.previous', [i for i in range(1111, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(224, '/telemetry.previous', [i for i in range(1112, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(225, '/telemetry.previous', [i for i in range(1113, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(226, '/telemetry.previous', [i for i in range(1115, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(227, '/telemetry.previous', [i for i in range(1116, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(228, '/telemetry.previous', [i for i in range(1117, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(229, '/telemetry.previous', [i for i in range(1119, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(230, '/telemetry.previous', [i for i in range(1121, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(231, '/telemetry.previous', [i for i in range(1122, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(232, '/telemetry.previous', [i for i in range(1123, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(233, '/telemetry.previous', [i for i in range(1126, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(234, '/telemetry.previous', [i for i in range(1127, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(235, '/telemetry.previous', [i for i in range(1129, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(236, '/telemetry.previous', [i for i in range(1130, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(237, '/telemetry.previous', [i for i in range(1131, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(238, '/telemetry.previous', [i for i in range(1133, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(239, '/telemetry.previous', [i for i in range(1134, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(240, '/telemetry.previous', [i for i in range(1135, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(241, '/telemetry.previous', [i for i in range(1137, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(242, '/telemetry.previous', [i for i in range(1138, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(243, '/telemetry.previous', [i for i in range(1139, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(244, '/telemetry.previous', [i for i in range(1141, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(245, '/telemetry.previous', [i for i in range(1142, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(246, '/telemetry.previous', [i for i in range(1143, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(247, '/telemetry.previous', [i for i in range(1145, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(248, '/telemetry.previous', [i for i in range(1146, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(249, '/telemetry.previous', [i for i in range(1147, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(250, '/telemetry.previous', [i for i in range(1148, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(251, '/telemetry.previous', [i for i in range(1149, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]

# 900 frames @ 9600 - 154.7mWh
