tasks = [
    # Generated on 2019-06-30 19:45:36.591000, contains telemetry from sessions 1380 to 1382.
    # The session starts on 2019-06-30 20:38:08+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(21, '/telemetry.current', [545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 570, 620]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 582, 632, 682, 732, 782, 832]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 552, 602, 652, 702, 752, 802, 852, 902]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [952, 1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [1176, 1226, 1276, 1326, 1376, 1426, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [1288, 1338, 1388, 1438]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p9_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p9_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p9_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p9_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p9_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/p9_480_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/p4_480_0', [66, 73, 74, 81, 88, 95, 98, 99, 100, 101]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/p4_480_0', [102, 103, 104, 105, 106, 107, 108, 112, 113, 114]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/p7_480_0', [21, 22, 23, 24, 25, 38, 74, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/p7_480_0', [87, 88, 89, 90, 91, 92, 116, 120, 123, 126, 127, 128, 130, 139]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/suns_ps_7', [23, 55, 59, 61, 62, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/suns_ps_7', [203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/suns_ps_7', [217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/p3_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/p3_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/p3_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/p3_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/p3_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/p1_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/p1_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/p1_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/p1_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/p1_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/p1_480_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/p1_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/p1_480_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/p7_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]