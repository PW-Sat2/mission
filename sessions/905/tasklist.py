tasks = [
    # Generated on 2019-04-20 21:46:05.843000, contains telemetry from sessions 904 to 905.
    # The session starts on 2019-04-20 23:04:33+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(58, '/telemetry.current', [1211, 1261, 1311, 1361, 1411, 1236, 1286, 1336, 1386, 1224, 1274, 1324, 1374, 1424, 1248, 1298, 1348, 1398, 1218, 1268]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [1318, 1368, 1418, 1230, 1280, 1330, 1380, 1430, 1242, 1292, 1342, 1392, 1254, 1304, 1354, 1404]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p5_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p3_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [172, 179, 185, 191, 203, 209, 215, 229, 235, 241, 247, 253, 259, 265, 279, 285, 291, 297, 303]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [309, 315, 329, 335, 341, 353, 359, 365, 379, 385, 391, 397, 403, 409, 415, 429, 435, 441, 447]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [453, 459, 465, 472, 479, 485, 491, 497, 503, 509, 515, 529, 535, 541, 547, 553, 559, 565, 579]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [585, 591, 597, 603, 609, 615, 629, 635, 641, 647, 653, 659, 665, 679, 685, 691, 703, 709, 715]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [722, 729, 735, 741, 753, 759, 765, 779, 785, 791, 797, 803, 809, 815, 829, 835, 841, 847, 853]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [859, 865, 879, 885, 891, 897, 903, 909, 915, 929, 935, 941, 947, 953, 959, 965, 979, 985, 991]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [997, 1003, 1009, 1015, 1029, 1035, 1041, 1047, 1053, 1059, 1065, 1079, 1085, 1091, 1097, 1103, 1109, 1115]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1129, 1135, 1141, 1147, 1153, 1159, 1165, 1172, 1179, 1185, 1191, 1197, 1203, 1209, 1215, 1222, 1229, 1235]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p7_128_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p2_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p6_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p10_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p9_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p1_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p1_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p1_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p1_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(60, 'radfet_11'), Send, WaitMode.Wait],
    [tc.ListFiles(61, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]