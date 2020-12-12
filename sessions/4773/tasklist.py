tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.RebootToNormal(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_53'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    #10:33
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_w_p480_0'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_n_p480_0'), Send, WaitMode.Wait],
    # 10:37 egipt
    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=4), 'b_w_p480_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_n_p480_1'), Send, WaitMode.Wait],
    #11:08 antarktyda
    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=31), 'b_w_p480_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'b_n_p480_2'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]