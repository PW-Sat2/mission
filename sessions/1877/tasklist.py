tasks = [
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 51, 101, 151, 201, 26, 76, 126, 176, 14, 64, 114, 164, 214, 38, 88, 138, 188, 8, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [108, 158, 208, 20, 70, 120, 170, 220, 32, 82, 132, 182, 44, 94, 144, 194]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing, part 1
    [tc.DownloadFile(200, '/radfet_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Made in China - photos of Himalayas and what else in Asia satellite will point at. - aim for 22:33, wait for 03:45
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_4'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_5'), Send, WaitMode.Wait],


    # Orbit 1, Japan, 03:45 - 03:47
    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=12), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(109, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(110, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.Wait],

    # Waiting from 03:47 to 06:57
    [tc.TakePhotoTelecommand(111, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_6'), Send, WaitMode.Wait],   
    [tc.TakePhotoTelecommand(112, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(113, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_8'), Send, WaitMode.Wait],


    # Orbit 2, China, Nepal, India, 06:57 - 07:03
    [tc.TakePhotoTelecommand(114, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=10), 't04w_480'), Send, WaitMode.Wait],
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

    [tc.TakePhotoTelecommand(126, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(127, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10n_480'), Send, WaitMode.Wait],

    # Waiting from 07:03 to 08:32
    [tc.TakePhotoTelecommand(128, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_9'), Send, WaitMode.Wait],   

    # Orbit 3, Middle East, 08:32 - 08:36
    [tc.TakePhotoTelecommand(129, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=29), 't11w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(130, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(131, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't12w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(133, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't13w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(134, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(135, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't14w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(136, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(137, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't15w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(138, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]