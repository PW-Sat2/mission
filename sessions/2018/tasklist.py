tasks = [
    # Generated on 2019-10-12 20:50:13.717000, contains telemetry from sessions 2017 to 2018.
    # The session starts on 2019-10-12 22:06:00+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(46, '/telemetry.current', [198, 248, 298, 348, 398, 223, 273, 323, 373, 211, 261, 311, 361, 411, 235, 285, 335, 385, 205, 255]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [305, 355, 405, 217, 267, 317, 367, 229, 279, 329, 379, 241, 291, 341, 391]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Part. 1 - Western Europe - aim for 22:11, wait for 23:43
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_6'), Send, WaitMode.Wait],

    # Orbit 1, 23:43 - 23:50
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=32), 't11w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't11n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't12w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(104, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't12n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't13w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't13n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't14w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't14n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(109, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't15w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(110, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't15n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(111, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't16w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't16n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(113, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't17w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(114, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't17n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(115, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't18w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(116, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't18n_480'), Send, WaitMode.Wait],

    # Part. 2 - USA - start 23:50 for wait for 06:04
    [tc.TakePhotoTelecommand(117, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_7'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(118, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_8'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(119, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_9'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(120, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_10'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(121, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_11'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(122, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_12'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(123, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=14), 't19w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(124, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't19n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(125, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't20w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(126, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't20n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(127, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't21w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(128, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't21n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(129, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't22w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(130, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't22n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(131, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't23w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(132, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't23n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(133, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't24w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(134, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't24n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(135, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't25w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(136, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't25n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(137, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't26w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(138, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't26n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],


    # auto-generated file download start
    [tc.DownloadFile(55, '/t01n_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t01n_480_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/t01w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t01w_480_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],

    [tc.DownloadFile(61, '/t02n_480_0', [ 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02n_480_0', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/t02w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t02w_480_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/t03n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t03n_480_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t03n_480_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/t03w_480_0', [12, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],

    [tc.DownloadFile(71, '/t04n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t04n_480_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t04n_480_0', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t04n_480_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t04w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t04w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t05n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t05n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t05n_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t05w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t05w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t06n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t06n_480_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t06n_480_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t06w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t06w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t07n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t07n_480_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t07n_480_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/t07w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t07w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/t08n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/t08n_480_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/t08n_480_0', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/t08w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/t08w_480_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/t08w_480_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/t09n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/t09n_480_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(200, '/t09n_480_0', [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/t09w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/t09w_480_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/t09w_480_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/t10n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/t10n_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/t10n_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(207, '/t10w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(208, '/t10w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(209, '/t10w_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],

    [tc.DownloadFile(48, '/dummy_1_0', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/dummy_2_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/dummy_2_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/dummy_3_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/dummy_3_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/dummy_4_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]