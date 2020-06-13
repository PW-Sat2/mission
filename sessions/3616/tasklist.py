tasks = [

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(3, 150, 110, 'radfet_40'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Group 1
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=3), 'p1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p5'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=2), 'p9'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]