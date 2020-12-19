tasks = [

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.little_oryx.RebootToNormal(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_54'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=30), 'p0_w_p480_0'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=10), 'p1_w_p480_0'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=10), 'p2_w_p480_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]