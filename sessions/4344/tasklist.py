tasks = [
   
    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # Wake-up from deep-sleep
    [[tc.PingTelecommand(), 15], SendLoop, WaitMode.NoWait],

    # Set bitrate
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Get few beacons from nominal OBC
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.PerformRadFETExperiment(100, 150, 110, 'radfet_48'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Photo queue - commands will be send ~22:36 cest
    # Terminator
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=4), 't_w_22_40'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 't_w_22_41'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=30), 't_w_22_42'), Send, WaitMode.Wait],


    # =========================================
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(20, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]