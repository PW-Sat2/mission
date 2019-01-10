tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # Take photo queue to test cameras
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p7_128'), Send, WaitMode.Wait],
    
    # auto-generated telemetry start
    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(1150, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(0, 450, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/telemetry.previous', [i for i in range(1174, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(12, 450, 24)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(24, '/telemetry.previous', [i for i in range(1156, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.previous', [i for i in range(1162, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.previous', [i for i in range(1168, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.previous', [i for i in range(1180, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.previous', [i for i in range(1186, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.previous', [i for i in range(1192, 2280, 48)]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(6, 450, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(18, 450, 24)]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(60, '/p6_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p6_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p7_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p7_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]