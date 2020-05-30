tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is photo (should be send ~12:13)", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - start ~12:16 cest
    # Group 1
    [tc.TakePhotoTelecommand(3, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=3), 'a1w_480_12_16'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(4, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a1n_480_12_16'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(5, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a2w_480_12_17'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(6, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a2n_480_12_17'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(7, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a3w_480_12_18'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(8, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a3n_480_12_18'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(9, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a4w_480_12_19'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a4n_480_12_19'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a5w_480_12_20'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a5n_480_12_20'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(13, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a6w_480_12_21'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a6n_480_12_21'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a7w_480_12_22'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a7n_480_12_22'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(17, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a8w_480_12_23'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(18, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a8n_480_12_23'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a9w_480_12_24'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a9n_480_12_24'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(21, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a10w_480_12_25'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(22, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a10n_480_12_25'), Send, WaitMode.Wait],

     # =========================================

    [tc.DownloadFile(23, '/radfet_39', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.DownloadFile(24, '/telemetry.current', [7, 57, 107, 157, 207, 32, 82, 132, 182, 20, 70, 120, 170, 220, 44, 94, 144, 194, 14, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [114, 164, 214, 26, 76, 126, 176, 226, 38, 88, 138, 188, 50, 100, 150, 200]), Send, WaitMode.Wait],

    [tc.ListFiles(26, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]