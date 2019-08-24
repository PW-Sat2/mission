tasks = [
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    # auto-generated telemetry end

    # 20th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_20'), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=1), 'x1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'x1_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'x2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(14, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'x2_480'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]