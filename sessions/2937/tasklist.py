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

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_33'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Normal
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=18), 't0w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't0n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't1w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't1n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't2w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(105, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't2n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(106, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't3w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't3n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(108, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't4w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(109, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't4n_480'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]