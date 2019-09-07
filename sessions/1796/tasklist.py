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

    # 21st RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_21'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Hurricane Dorian hunting - aim for 11:50, wait for 16:40
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_4'), Send, WaitMode.Wait],

    # Orbit 1, 16:40 - 16:45
    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=50), 't01w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(107, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't01n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(109, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't02w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(110, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(111, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't02n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(113, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't03w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(114, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(115, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't03n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(116, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(117, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't04w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(118, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't04w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(119, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't04n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(120, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't04n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(121, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't05w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(122, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(123, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't05n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(124, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(125, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't06w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(126, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't06w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(127, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't06n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(128, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't06n_480'), Send, WaitMode.Wait],

    # Waiting from 16:40 to 18:15
    [tc.TakePhotoTelecommand(129, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_5'), Send, WaitMode.Wait],

    # Orbit 2, 18:15 - 18:22
    [tc.TakePhotoTelecommand(130, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=30), 't07w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(131, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't07n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(133, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(134, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't08w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(135, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(136, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't08n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(137, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(138, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't09w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(139, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(140, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't09n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(141, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(142, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't10w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(143, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(144, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't10n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(145, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(146, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't11w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(147, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(148, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't11n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(149, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(150, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't12w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(151, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(152, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't12n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(153, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(154, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't13w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(155, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(156, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't13n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(157, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(158, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(seconds=20), 't14w_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(159, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(160, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(seconds=0), 't14n_128'), Send, WaitMode.Wait], 
    [tc.TakePhotoTelecommand(161, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]