tasks = [
    # Generated on 2020-01-31 23:19:31.748000, contains telemetry from sessions 2749 to 2751.
    # The session starts on 2020-02-01 10:17:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773, 823, 873, 923, 973, 1023, 1073, 1123]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1173, 1223, 1273, 1323, 1373, 1423, 1473, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 186, 236, 286, 336, 386, 436, 486]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 210]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1260, 1310, 1360, 1410, 1460, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [930, 980, 1030, 1080, 1130, 1180, 1230, 1280, 1330, 1380, 1430, 192, 242, 292, 342, 392, 442, 492, 542, 592]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [642, 692, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 204, 254, 304]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1354, 1404, 1454, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(41, '/t02w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t02w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t02w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t02w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t02w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t02w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t02w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t02w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t02w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t02w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t02w_240_10', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t02w_240_11', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t02w_240_12', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t02w_240_13', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t02w_240_14', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t02w_240_15', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t02w_240_16', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t02w_240_17', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t02w_240_18', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t02w_240_19', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t02w_240_20', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02w_240_21', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t02w_240_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t02w_240_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t02w_240_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t02w_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t02w_240_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t02w_240_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t02w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t03w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t03w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t03w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t03w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t03w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t03w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t03w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t03w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t03w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t03w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t03w_240_10', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t03w_240_11', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t03w_240_12', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t03w_240_13', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t03w_240_14', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t03w_240_15', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t03w_240_16', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t03w_240_17', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/t03w_240_18', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/t03w_240_19', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/t03w_240_20', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/t03w_240_21', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/t03w_240_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/t03w_240_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/t03w_240_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/t03w_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/t03w_240_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/t03w_240_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/t03w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/t04w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/t04w_240_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/t04w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/t04w_240_1', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/t04w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/t04w_240_2', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/t04w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/t04w_240_3', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/t04w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/t04w_240_4', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/t04w_240_4', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/t04w_240_4', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/t04w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/t04w_240_5', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/t04w_240_5', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/t04w_240_5', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/t04w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/t04w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/t04w_240_6', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]