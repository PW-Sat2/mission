tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_45'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - commands will be send ~11:27 cest
    # Russia/Ukraine
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_28'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_28'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_29'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_29'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_30'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_30'), Send, WaitMode.Wait],

    # Mediterranean sea & Africa
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=3), 'a_w_11_33'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_33'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_34'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_34'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_35'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_35'), Send, WaitMode.Wait],

    # South Africa
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=14), 'a_w_11_49'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_49'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_50'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_50'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_51'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_51'), Send, WaitMode.Wait],

    # Scandinavia
    [tc.TakePhotoTelecommand(24, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=67), 'a_w_12_58'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_58'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_12_59'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_59'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(28, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_00'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_00'), Send, WaitMode.Wait],


    # =========================================


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]