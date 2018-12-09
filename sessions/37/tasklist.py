tasks = [
    [[tc.SetBitrate(73, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(83, '/'), Send, WaitMode.Wait],

    # Telemetry between session 36 and 37
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1950, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 800, 100)]), Send, WaitMode.Wait],

    # Photos scheduled
    [tc.TakePhotoTelecommand(101, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(111, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(121, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(122, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(131, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(141, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(142, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    [tc.SetBitrate(93, 8), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
