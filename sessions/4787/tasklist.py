tasks = [
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
    [tc.little_oryx.RebootToNormal(), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    #12:42 - schedule photos
    [tc.TakePhotoTelecommand(7, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=60), 'x_13_42'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=60), 'x_14_42'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=60), 'x_15_42'), Send, WaitMode.Wait],

    #16:10 - maximum visible eclipse part 1
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=26), 'w_16_08'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_16_08'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_16_09'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_16_09'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_16_10'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_16_10'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(16, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_16_11'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_16_11'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_16_12'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_16_12'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(20, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=60), 'x_17_11'), Send, WaitMode.Wait],

    #17:44 - maximum visible eclipse part 2
    [tc.TakePhotoTelecommand(21, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=30), 'w_17_41'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(22, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_41'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_17_42'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_42'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(25, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_17_43'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(26, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_43'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_17_44'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_44'), Send, WaitMode.Wait],
    
    [tc.TakePhotoTelecommand(29, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_17_45'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(30, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_45'), Send, WaitMode.Wait],
  
    [tc.TakePhotoTelecommand(31, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 'w_17_46'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(32, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'n_17_46'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]