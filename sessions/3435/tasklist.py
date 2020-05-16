tasks = [

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is photo (should be sent ~12:55)", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - start ~12:56 cest
    # Group 1
    [tc.TakePhotoTelecommand(3, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm1w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(4, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm1n_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(5, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm2w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(6, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm2n_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(7, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm3w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(8, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm3n_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(9, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm4w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm4n_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm5w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm5n_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(13, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm6w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm6n_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm7w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm7n_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(17, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm8w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(18, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm8n_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'm9w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'm9n_480'), Send, WaitMode.Wait],

     # =========================================

    [tc.DownloadFile(21, '/radfet_38', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(22, '/telemetry.current', [5, 55, 105, 155, 205, 30, 80, 130, 180, 18, 68, 118, 168, 218, 42, 92, 142, 192, 12, 62]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(23, '/telemetry.current', [112, 162, 212, 24, 74, 124, 174, 224, 36, 86, 136, 186, 48, 98, 148, 198]), Send, WaitMode.Wait],

    [tc.ListFiles(24, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]