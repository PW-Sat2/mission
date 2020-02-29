tasks = [
    # Generated on 2020-02-29 23:42:29.024000, contains telemetry from sessions 2939 to 2940.
    # The session starts on 2020-03-01 09:10:03+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(45, '/telemetry.current', [351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1351, 1401, 1451, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1226, 1276, 1326, 1376, 1426, 1476, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 1464, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 358, 408, 458, 508, 558, 608, 658, 708, 758]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 370, 420, 470, 520, 570, 620]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 382, 432, 482]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [1394, 1444]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t0w_480_0', [113]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t1n_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t1n_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t2w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t2w_480_0', [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t2w_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t2w_480_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t2w_480_0', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t4n_480_0', [60, 61, 68, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t4n_480_0', [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t4n_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t4n_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t4w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t4w_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t4w_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]