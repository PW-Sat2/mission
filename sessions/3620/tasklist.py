tasks = [
    # Generated on 2020-06-13 20:46:24.654000, contains telemetry from sessions 3617 to 3620.
    # The session starts on 2020-06-13 22:05:48+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Bit earlier, because I need time used normally for downloading telemetry.
    # Group 1
    [tc.TakePhotoTelecommand(4, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't1w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(5, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't1n'), Send, WaitMode.Wait],

    # Group 2
    [tc.TakePhotoTelecommand(6, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't2w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(7, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't2n'), Send, WaitMode.Wait],

    # Group 3
    [tc.TakePhotoTelecommand(8, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't3w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(9, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't3n'), Send, WaitMode.Wait],

    # Group 4
    [tc.TakePhotoTelecommand(10, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't4w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(11, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't4n'), Send, WaitMode.Wait],

    # Group 5
    [tc.TakePhotoTelecommand(12, CameraLocation.Wing, PhotoResolution.p480, 1, datetime.timedelta(minutes=1), 't5w'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(13, CameraLocation.Nadir, PhotoResolution.p480, 1, datetime.timedelta(minutes=0), 't5n'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(64, '/telemetry.current', [172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [1172, 1222, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [1097, 1147, 1197, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [1035, 1085, 1135, 1185, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [1009, 1059, 1109, 1159, 1209, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [929, 979, 1029, 1079, 1129, 1179, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [891, 941, 991, 1041, 1091, 1141, 1191, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [853, 903, 953, 1003, 1053, 1103, 1153, 1203, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 145]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(41, '/p4_0', [120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],  
    [tc.DownloadFile(32, '/p10_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p5_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p6_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p7_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p8_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p9_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/p5_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p5_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p5_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p5_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p5_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p5_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p5_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p6_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p6_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p6_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p7_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p7_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p7_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p7_0', [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p8_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p8_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p8_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p9_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p9_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p9_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p9_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p10_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p10_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p10_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait], 

    [tc.ListFiles(201, '/'), Send, WaitMode.Wait],
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]