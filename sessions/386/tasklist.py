tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(12, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(14, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(15, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(16, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(17, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(18, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(19, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(20, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(21, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(22, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(23, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(24, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(25, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(26, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(27, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(28, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(29, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],
    
    # =========================================

    ["The next step is telemetry download.", Print, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1139, 1189, 1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]