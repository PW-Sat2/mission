tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 118 and 119
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1700, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1706, 1900, 12)]), Send, WaitMode.Wait],

    # TakePhoto queue - ASAP
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(70, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=30), 'p11_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(71, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p11_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(72, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=30), 'p12_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(73, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p12_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(74, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=30), 'p13_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(75, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p13_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(76, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=30), 'p14_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p14_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(78, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=30), 'p15_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(79, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p15_480'), Send, WaitMode.Wait],

    # Remove photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(40, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(44, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(45, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(46, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(47, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(48, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(49, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(50, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(51, '/p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(52, '/p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(53, '/p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(54, '/p5_480_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(55, '/p6_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(56, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(57, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(58, '/p9_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(59, '/p10_480_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(60, '/suns_7'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, '/suns_7_sec'), Send, WaitMode.NoWait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # More telemetry between session 118 and 119
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1703, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1709, 1900, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1701, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1702, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1704, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1705, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(1707, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(1708, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(1710, 1900, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(1711, 1900, 12)]), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]