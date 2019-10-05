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

    # 23rd RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_23'), Send, WaitMode.Wait],

    # Check if sail is still there
    [tc.TakePhotoTelecommand(210, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(211, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(213, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]