tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_43'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - commands will be send ~12:44 cest
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_12_46'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_46'), Send, WaitMode.Wait],


    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_12_48'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_48'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_12_50'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_12_50'), Send, WaitMode.Wait],

    # Night start
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=39), 'a_n_13_29'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=39), 'a_n_14_08'), Send, WaitMode.Wait],
    # Night end

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_14_10'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_14_10'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_14_12'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_14_12'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_14_14'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_14_14'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'a_w_14_16'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'a_n_14_16'), Send, WaitMode.Wait],


    # =========================================


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]