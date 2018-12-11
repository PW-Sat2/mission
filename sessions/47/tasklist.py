tasks = [
    [[tc.SetBitrate(40, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(41, '/'), Send, WaitMode.Wait],

    # Remove old experiment files
    [tc.RemoveFile(42, '/radfet'), Send, WaitMode.Wait],
    [tc.RemoveFile(43, '/p2_480_0'), Send, WaitMode.Wait],
    [tc.ListFiles(44, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 42 and 43
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(0, 250, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(12, 250, 25)]), Send, WaitMode.Wait],

    # Take 50 low-res photos
    [tc.TakePhotoTelecommand(73, CameraLocation.Nadir, PhotoResolution.p128, 29, datetime.timedelta(minutes=45), 'hor'), Send, WaitMode.Wait],

    # Much more telemetry between 42 and 43
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(4, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(8, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(16, 1000, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(53, '/telemetry.previous', [i for i in range(20, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(32, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(38, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(46, 1000, 50)]), Send, WaitMode.Wait],

    # Much more telemetry between 42 and 43
    [tc.DownloadFile(60, '/telemetry.previous', [i for i in range(1004, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [i for i in range(1008, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [i for i in range(1016, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(63, '/telemetry.previous', [i for i in range(1020, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.previous', [i for i in range(1032, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.previous', [i for i in range(1038, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.previous', [i for i in range(1046, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
