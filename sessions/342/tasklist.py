tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["The next step is Take Photo.", Print, WaitMode.Wait],

    # Photo queue
    # Group 1
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(40, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=0), 'p1_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(41, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p1_480'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(42, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p2_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(43, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p2_480'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(44, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p3_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(45, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p3_480'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(46, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p4_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(47, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p4_480'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(48, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p5_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(49, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p5_480'), Send, WaitMode.Wait],

    # Group 6
    [tc.TakePhotoTelecommand(50, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p6_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(51, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p6_480'), Send, WaitMode.Wait],

    # Group 7
    [tc.TakePhotoTelecommand(52, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p7_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(53, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p7_480'), Send, WaitMode.Wait],

    # Group 8
    [tc.TakePhotoTelecommand(54, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p8_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(55, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p8_480'), Send, WaitMode.Wait],

    # Group 9
    [tc.TakePhotoTelecommand(56, CameraLocation.Wing, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p9_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(57, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p9_480'), Send, WaitMode.Wait],

    # Group 10
    [tc.TakePhotoTelecommand(58, CameraLocation.Nadir, PhotoResolution.p128, 1, datetime.timedelta(minutes=4), 'p10_128'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(59, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 'p10_480'), Send, WaitMode.Wait],
    # =========================================

    ["The next step is telemetry download.", Print, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(60, '/telemetry.previous', [2170, 2220, 2270, 2195, 2245, 2183, 2233, 2207, 2257, 2177, 2227, 2277, 2189, 2239, 2201, 2251, 2213, 2263]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [1040, 1090, 1140, 1190, 1240, 1290, 1340, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 3, 53, 103, 153, 203]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [1253, 1303, 1353, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 47, 97, 147, 197, 247, 297, 347, 397, 447]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [1109, 1159, 1209, 1259, 1309, 1359, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 33, 83, 133, 183, 233, 283]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [1333]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    [tc.ListFiles(80, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]