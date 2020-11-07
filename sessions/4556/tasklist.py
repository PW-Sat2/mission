tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.RebootToNormal(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_49'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'n_w_0'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_0'), Send, WaitMode.Wait],


    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_1'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_2'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=32), 'n_w_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_3'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_4'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_4'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_5'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_5'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=42), 'n_w_6'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_6'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_7'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'n_w_8'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_n_8'), Send, WaitMode.Wait],


    # =========================================


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]