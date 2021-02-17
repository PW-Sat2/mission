tasks = [
    # Generated on 2021-02-18 00:22:00.036000, contains telemetry from sessions 5176 to 5177.
    # The session starts on 2021-02-18 11:12:49+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(43, '/telemetry.current', [429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1429, 1479, 1529, 1579, 1629, 1679, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 442, 492, 542, 592, 642, 692, 742, 792, 842]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 466, 516, 566, 616]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1666, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 1336]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1386, 1436, 1486, 1536, 1586, 1636, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 460, 510, 560, 610, 660, 710, 760, 810, 860]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 472, 522, 572, 622]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(33, '/p5174_0_n_p480_0', [69, 78, 90, 91, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5174_0_n_p480_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p5174_1_w_p480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p5174_1_w_p480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p5174_1_w_p480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p5174_1_w_p480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p5174_1_w_p480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p5174_1_w_p480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p5174_1_w_p480_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p5174_1_w_p480_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p5174_1_w_p480_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]