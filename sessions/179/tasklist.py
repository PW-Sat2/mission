tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    [tc.SendBeacon(), Send, WaitMode.Wait], # Wait until good communication
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(6, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(8, '/'), Send, WaitMode.Wait],

    # Telemetry between session 176 and 179
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(0, 600, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1800, 2280, 24)]), Send, WaitMode.Wait],

    # TakePhoto queue - start 20:30
    # Group 1 - Alaska
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(70, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=15), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(71, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(72, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(73, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(74, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(75, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(76, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(77, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5 - Hawaii
    [tc.TakePhotoTelecommand(78, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=10), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(79, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(80, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(81, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7 - Antarctica
    [tc.TakePhotoTelecommand(82, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=25), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(83, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(84, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(85, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(86, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(87, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(88, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(89, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],

    # More telemetry between session 176 and 179
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(24, 600, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1812, 2280, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(12, 600, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(36, 600, 48)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]