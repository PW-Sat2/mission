tasks = [
     [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Super Long Photos Part 1 - aim into 22:43

    # Orbit 1, 23:02, 60 N, Alaska
    [tc.TakePhotoTelecommand(200, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=19), 't01w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(201, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(202, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't01n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(203, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.NoWait],

    # Orbit 1, 23:09, 40 N, ocean
    [tc.TakePhotoTelecommand(204, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't02w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(205, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't02n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 1, time extender
    [tc.TakePhotoTelecommand(206, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_1'), Send, WaitMode.Wait],
 
    # Orbit 2, 00:38, 60 N, more Alaska
    [tc.TakePhotoTelecommand(207, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't03w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(208, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(209, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't03n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(210, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.NoWait],

    # Orbit 2, 00:45, 40 N, ocean
    [tc.TakePhotoTelecommand(211, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't04w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't04n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 2, time extender
    [tc.TakePhotoTelecommand(213, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_2'), Send, WaitMode.Wait],
 
    # Orbit 3, 02:14, 60 N, Siberia
    [tc.TakePhotoTelecommand(214, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't05w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(215, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(216, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't05n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(217, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05n_480'), Send, WaitMode.NoWait],

    # Orbit 3, 02:21, 40 N, ocean
    [tc.TakePhotoTelecommand(218, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't06w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(219, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't06n_128'), Send, WaitMode.NoWait], 
 
    # Orbit 3, time extender
    [tc.TakePhotoTelecommand(220, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_3'), Send, WaitMode.Wait],
 
    # Orbit 4, 03:57, 40 N, Japan
    [tc.TakePhotoTelecommand(221, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't07w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(222, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(223, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't07n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(224, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07n_480'), Send, WaitMode.Wait],

    # Orbit 4, time extender
    [tc.TakePhotoTelecommand(225, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_4'), Send, WaitMode.Wait],
 
    # Orbit 5, 05:33, 40 N, China
    [tc.TakePhotoTelecommand(226, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't08w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(227, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(228, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't08n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(229, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08n_480'), Send, WaitMode.Wait],

    # Orbit 5, time extender
    [tc.TakePhotoTelecommand(230, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_5'), Send, WaitMode.Wait],
 
    # Orbit 6, 07:09, 40 N, Tibet
    [tc.TakePhotoTelecommand(231, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't09w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(232, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(233, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't09n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(234, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09n_480'), Send, WaitMode.Wait],

    # Orbit 6, 07:11, Himalayas
    [tc.TakePhotoTelecommand(235, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=2), 't10w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(236, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(237, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't10n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(238, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10n_480'), Send, WaitMode.Wait],

    # Orbit 6, time extender
    [tc.TakePhotoTelecommand(239, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_6'), Send, WaitMode.Wait],
 
    # Orbit 7, 08:45, 40 N, Pakistan or somewhere there
    [tc.TakePhotoTelecommand(240, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=34), 't11w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(241, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11w_480'), Send, WaitMode.NoWait],
    [tc.TakePhotoTelecommand(242, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't11n_128'), Send, WaitMode.NoWait], 
    [tc.TakePhotoTelecommand(243, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11n_480'), Send, WaitMode.NoWait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]