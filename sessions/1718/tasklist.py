tasks = [
     [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Super Long Photos Part 2 - aim into 11:52

    # Orbit 8, 11:57, 40 N, Italy
    [tc.TakePhotoTelecommand(200, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=5), 't12w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(201, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(202, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't12n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(203, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12n_480'), Send, WaitMode.Wait],

    # Orbit 8, time extender
    [tc.TakePhotoTelecommand(204, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_7'), Send, WaitMode.Wait],
 
    # Orbit 9, 13:29, 50 N, UK
    [tc.TakePhotoTelecommand(205, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=32), 't13w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(206, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(207, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't13n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(208, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13n_480'), Send, WaitMode.Wait],

    # Orbit 9, 13:33, 40 N, Portugal
    [tc.TakePhotoTelecommand(209, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 't14w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(210, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(211, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't14n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(212, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14n_480'), Send, WaitMode.Wait],

    # Orbit 9, time extender
    [tc.TakePhotoTelecommand(213, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_8'), Send, WaitMode.Wait],
 
    # Orbit 10, 15:02, 60 N, Island
    [tc.TakePhotoTelecommand(214, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=29), 't15w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(215, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(216, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't15n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(217, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15n_480'), Send, WaitMode.Wait],

    # Orbit 10, 15:09, 40 N, ocean
    [tc.TakePhotoTelecommand(218, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=7), 't16w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(219, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't16n_128'), Send, WaitMode.Wait], 
 
    # Orbit 10, time extender
    [tc.TakePhotoTelecommand(220, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_9'), Send, WaitMode.Wait],
 
    # Orbit 11, 16:36, 60 N, Greenland
    [tc.TakePhotoTelecommand(221, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=27), 't17w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(222, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't17w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(223, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't17n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(224, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't17n_480'), Send, WaitMode.Wait],

    # Orbit 11, 16:45, 40 N, ocean
    [tc.TakePhotoTelecommand(225, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=9), 't18w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(226, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't18n_128'), Send, WaitMode.Wait], 
 
    # Orbit 11, time extender
    [tc.TakePhotoTelecommand(227, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_10'), Send, WaitMode.Wait],
 
    # Orbit 12, 18:21, 40 N, USA East
    [tc.TakePhotoTelecommand(228, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't19w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(229, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't19w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(230, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't19n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(231, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't19n_480'), Send, WaitMode.Wait],

    # Orbit 12, time extender
    [tc.TakePhotoTelecommand(232, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=30), 'dummy_11'), Send, WaitMode.Wait],
 
    # Orbit 13, 19:57, 40 N, USA West
    [tc.TakePhotoTelecommand(233, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=36), 't20w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(234, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't20w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(235, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't20n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(236, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't20n_480'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]