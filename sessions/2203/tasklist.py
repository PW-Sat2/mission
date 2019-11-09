tasks = [
    # Generated on 2019-11-09 02:41:57.575950, contains telemetry from sessions 2201 to 2203.
    # The session starts on 2019-11-09 09:21:27+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1001, 1051, 1101, 1151, 1201, 1251, 1301, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176, 1226, 1276, 14, 64, 114, 164, 214, 264, 314]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1088, 1138, 1188, 1238, 1288, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 20, 70, 120, 170, 220, 270, 320, 370]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 32, 82]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1132, 1182, 1232, 1282, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    [tc.DownloadFile(41, '/radfet_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    # auto-generated file download end

    [tc.DownloadFile(50, '/t01w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t01n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/t02w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t02n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/t03w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t03n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/t04w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t04n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/t05w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t05n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/t06w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t06n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/t07w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t07n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/t08w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t08n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/t09w_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t09n_480', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]