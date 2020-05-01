tasks = [

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is photo (should be send ~22:53)", Print, WaitMode.Wait],

    # Photo queue - start ~23:00 cest
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(3, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=7), 'a1w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(4, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a1n_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(5, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a2w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(6, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a2n_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(7, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a3w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(8, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=30), 'a3n_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(9, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a4w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a4n_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a5w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a5n_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(13, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a6w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a6n_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a7w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a7n_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(17, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a8w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(18, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a8n_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'a9w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a9n_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(21, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=19), 'a10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(22, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a10n_480'), Send, WaitMode.Wait],

     # =========================================


    [tc.ListFiles(23, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]