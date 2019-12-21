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

    ["Becons and photos", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

     # Long Movie Over Europe, don't have to wait
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(minutes=1), 't01w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(seconds=0), 't02w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(seconds=0), 't03w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p240, 7, datetime.timedelta(seconds=0), 't04w_240'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]