tasks = [
    # Generated on 2019-10-12 09:23:29.222000, contains telemetry from sessions 2011 to 2014.
    # The session starts on 2019-10-12 11:14:49+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [528, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Part. 1 - Korea by night - aim for 11:20, wait for 15:40
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_1'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_2'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_3'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(104, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=59, seconds=50), 'dummy_4'), Send, WaitMode.Wait],

    # Orbit 1, 15:40-15:49
    [tc.TakePhotoTelecommand(105, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=20), 't01w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(106, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't01n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(107, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't02w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(108, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't02n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(109, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't03w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(110, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't03n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(111, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't04w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(112, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't04n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(113, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't05w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(114, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't05n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(115, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't06w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(116, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't06n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(117, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't07w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(118, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't07n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(119, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't08w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(120, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't08n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(121, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't09w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(122, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't09n_480'), Send, WaitMode.Wait],

    [tc.TakePhotoTelecommand(123, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(seconds=20), 't10w_480'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(124, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(seconds=0), 't10n_480'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]