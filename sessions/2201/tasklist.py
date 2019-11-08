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
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_25'), Send, WaitMode.Wait],

    # Waste session time
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Bombay Calling - wait for 21:55
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_4'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_5'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_6'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_8'), Send, WaitMode.Wait],
 
    # Orbit 1, India, in hope of another Typhoon, 06:20 - 06:28
    [tc.TakePhotoTelecommand(108, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=25), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(109, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(110, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(111, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(112, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(113, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(114, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't04w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(115, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't04n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(116, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(117, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(118, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't06w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(119, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't06n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(120, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't07w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(121, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(122, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't08w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(123, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(124, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't09w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(125, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09n_480'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]