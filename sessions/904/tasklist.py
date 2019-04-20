tasks = [
    # Generated on 2019-04-20 20:34:29.748000, contains telemetry from sessions 901 to 904.
    # The session starts on 2019-04-20 21:29:39+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1172, 1222, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1097, 1147, 1197, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1035, 1085, 1135, 1185, 1235, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [959, 1009, 1059, 1109, 1159, 1209, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [879, 929, 979, 1029, 1079, 1129, 1179, 1229, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(39, '/p2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p2_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p3_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p6_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p7_128_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p9_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p9_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p10_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p1_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p1_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p1_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p1_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p1_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(61, 'radfet_11'), Send, WaitMode.Wait],
    [tc.ListFiles(62, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]