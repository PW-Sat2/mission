tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_42'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - commands will be send ~12:26 cest
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_12_28'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_28'), Send, WaitMode.Wait],


    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_12_29'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_29'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_12_30'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_30'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=32), 'a_w_13_02'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_02'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_03'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_03'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_04'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_04'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=42), 'a_w_13_46'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_46'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_47'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_47'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_48'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_48'), Send, WaitMode.Wait],


    # =========================================


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]