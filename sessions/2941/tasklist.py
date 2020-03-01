tasks = [
    # Generated on 2020-03-01 09:29:55.646000, contains telemetry from sessions 2940 to 2941.
    # The session starts on 2020-03-01 10:43:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [1451, 1501, 1551, 1601, 1651, 1476, 1526, 1576, 1626, 1464, 1514, 1564, 1614, 1664, 1488, 1538, 1588, 1638, 1458, 1508]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1558, 1608, 1658, 1470, 1520, 1570, 1620, 1670, 1482, 1532, 1582, 1632, 1494, 1544, 1594, 1644]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [370, 382, 394, 420, 432, 438, 444, 470, 482, 488, 494, 520, 532, 538, 544, 570, 582, 588]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [594, 620, 632, 644, 670, 682, 694, 720, 732, 744, 770, 782, 794, 808, 820, 832, 844, 858]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [870, 882, 894, 908, 920, 932, 944, 958, 970, 982, 994, 1008, 1020, 1032, 1044, 1058, 1070, 1082]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1094, 1108, 1114, 1120, 1132, 1144, 1158, 1164, 1170, 1182, 1194, 1208, 1220, 1232, 1244, 1258, 1270, 1282]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1294, 1308, 1320, 1332, 1344, 1358, 1370, 1382, 1388, 1394, 1408, 1414, 1420, 1432, 1444, 1458, 1470, 1482]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t0w_480_0', [113]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t1n_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t1n_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t4w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t4w_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t4w_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t4n_480_0', [60, 61, 68, 70, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t4n_480_0', [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t4n_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t4n_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t2w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t2w_480_0', [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t2w_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t2w_480_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t2w_480_0', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]