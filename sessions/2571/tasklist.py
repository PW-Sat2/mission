tasks = [
    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Wake-up from deep-sleep
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Get beacon
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],
  
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_29'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Padawan's Photos, 20:18
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=12), 'p01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(105, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p03n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(106, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p04w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p04n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(108, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(109, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p05n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(110, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 'p06w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(111, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 'p06n_480'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]