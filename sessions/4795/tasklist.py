tasks = [
    # Generated on 2020-12-15 13:57:29.883995, contains telemetry from sessions 4793 to 4795.
    # The session starts on 2020-12-15 21:14:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(99, '/telemetry.current', [311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [1311, 336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [1286, 1336, 324, 374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [1224, 1274, 1324, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [1198, 1248, 1298, 1348, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [1118, 1168, 1218, 1268, 1318, 330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [1080, 1130, 1180, 1230, 1280, 1330, 342, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [1042, 1092, 1142, 1192, 1242, 1292, 1342, 354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [311, 318, 324, 330, 336, 342, 348, 354, 361, 368, 374, 380, 386, 392, 398, 404, 411, 418]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [424, 430, 436, 442, 448, 454, 461, 468, 474, 480, 486, 492, 498, 504, 511, 518, 524, 530]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1173, 1592, 1642, 1654, 1736]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n_16_12_0', [18, 19, 20, 21, 23, 48, 56, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n_17_41_0', [29, 30, 72, 92, 97, 98, 106, 107, 111, 128, 132, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n_17_43_0', [150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/n_17_46_0', [52, 67, 68, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/w_16_08_0', [11, 12, 13, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/w_16_08_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/w_16_08_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/w_16_08_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/w_16_08_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/w_16_09_0', [10, 11, 12, 13, 14, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/w_16_09_0', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/w_16_09_0', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/w_16_09_0', [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/w_16_10_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/w_16_10_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/w_16_10_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/w_16_10_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/w_16_10_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/w_16_10_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/w_16_10_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/w_16_10_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/w_16_11_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/w_16_11_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/w_16_11_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/w_16_12_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/w_16_12_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/w_16_12_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/w_16_12_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/w_16_12_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/w_16_12_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/w_16_12_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/w_16_12_0', [143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/w_17_41_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/w_17_41_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/w_17_41_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/w_17_41_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/w_17_42_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/w_17_42_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/w_17_42_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/w_17_42_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/w_17_42_0', [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/w_17_42_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/w_17_43_0', [11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/w_17_43_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/w_17_43_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/w_17_43_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/w_17_43_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/w_17_43_0', [104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/w_17_43_0', [121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/w_17_45_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/w_17_45_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/w_17_45_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/w_17_45_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/w_17_45_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/w_17_45_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/w_17_45_0', [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/w_17_46_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/w_17_46_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/w_17_46_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/w_17_46_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/w_17_46_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/w_17_46_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/w_17_46_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/w_17_46_0', [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/x_14_42_0', [6, 7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/x_17_11_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]