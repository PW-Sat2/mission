tasks = [
    # Generated on 2019-05-05 13:31:06.029899, contains telemetry from sessions 1005 to 1006.
    # The session starts on 2019-05-05 20:37:28+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 570, 620]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 582, 632, 682, 732, 782, 832]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 552, 602, 652, 702, 752, 802, 852, 902]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [952, 1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1176, 1226, 1276, 1326, 1376, 1426, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1288, 1338, 1388, 1438]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(38, '/p9_128_0', [25]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [393, 405, 417, 443, 455, 467, 481, 493, 505, 517, 531, 543, 555, 567, 581, 593]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p2_480_0', [39, 42, 43, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p2_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p2_480_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p2_480_0', [103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p2_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p2_480_0', [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p2_480_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p8_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p8_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p8_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p8_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p8_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p8_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p8_480_0', [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p8_480_0', [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]