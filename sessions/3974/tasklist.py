tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_44'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - commands will be send ~11:25 cest
    # Europe/Turkey/Africa
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=5), 'a_w_11_30'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_30'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_31'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_31'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_32'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_32'), Send, WaitMode.Wait],

    # Central Africa
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=8), 'a_w_11_40'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_40'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_41'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_41'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_42'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_42'), Send, WaitMode.Wait],

    # Sunset over Antarctica
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=15), 'a_w_11_57'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_57'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_58'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_58'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_11_59'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_11_59'), Send, WaitMode.Wait],

    # Scandinavia
    [tc.TakePhotoTelecommand(24, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=60), 'a_w_12_59'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_59'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_00'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_00'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(28, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'a_w_13_01'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_13_01'), Send, WaitMode.Wait],


    # =========================================


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]