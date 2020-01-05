tasks = [
    # Generated on 2020-01-04 23:37:40.361000, contains telemetry from sessions 2573 to 2574.
    # The session starts on 2020-01-05 09:17:11+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(51, '/telemetry.current', [354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1354, 1404, 1454, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1229, 1279, 1329, 1379, 1429, 1479, 367, 417, 467, 517, 567, 617, 667, 717, 767, 817, 867, 917, 967, 1017]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 361, 411, 461, 511, 561, 611, 661, 711, 761]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 373, 423, 473, 523, 573, 623]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [673, 723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 385, 435, 485]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [1397, 1447]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p03n_480_0', [106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p03n_480_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p03w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p03w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p03w_480_0', [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p04w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p04w_480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p04w_480_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p04w_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p04w_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p05n_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p05n_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p05w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p05w_480_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p06n_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p06n_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p06w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p06w_480_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p06w_480_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p06w_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p06w_480_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]