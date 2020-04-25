tasks = [
    # Generated on 2020-03-13 20:58:59.843000, contains telemetry from sessions 3022 to 3023.
    # The session starts on 2020-03-13 21:49:15+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue - start 11:24
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't1w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't1n_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(13, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=3), 't2w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't2n_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't3w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 't3n_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(17, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 't4w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(18, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't4n_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 't5w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't5n_480'), Send, WaitMode.Wait],


    [tc.TakePhotoTelecommand(121, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=60), 'dummy1'), Send, WaitMode.Wait],
    

    # Group 6
    [tc.TakePhotoTelecommand(21, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=6), 't6w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(22, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't6n_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=6), 't7w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't7n_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(25, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=6), 't8w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(26, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't8n_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 't9w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't9n_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(29, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(30, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't10n_480'), Send, WaitMode.Wait],
    
    # Group 11
    [tc.TakePhotoTelecommand(31, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 't11w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(32, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't11n_480'), Send, WaitMode.Wait],
   
    # =========================================
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_35'), Send, WaitMode.Wait],

     # =========================================


    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]