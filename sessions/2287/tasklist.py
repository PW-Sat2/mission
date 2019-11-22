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

    # 24rd RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_26'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # The Satellite of the Rising Sun - wait for 21:19
    [tc.TakePhotoTelecommand(42, CameraLocation.Nadir, PhotoResolution.p240, 29, datetime.timedelta(minutes=7), 't01w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Nadir, PhotoResolution.p240, 29, datetime.timedelta(minutes=0), 't02w_240'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]