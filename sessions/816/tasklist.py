tasks = [
    # Generated on 2019-04-07 14:17:50.882000, contains telemetry from sessions 815 to 816.
    # The session starts on 2019-04-07 20:50:05+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/suns_ps_3', [163, 173, 177, 180, 181, 184, 185, 186, 188, 189, 190, 191, 192, 193]), Send, WaitMode.Wait],
	[tc.DownloadFile(21, '/suns_ps_3', [194, 195, 196, 197, 198, 200, 201, 203, 204, 205, 206, 210, 214, 216]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 744, 794]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 732, 782, 832, 882]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 756, 806, 856, 906, 956, 1006]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 726, 776, 826, 876, 926, 976, 1026, 1076]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1238, 1288, 1338, 1388, 1438, 1488, 1538, 1588, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1350, 1400, 1450, 1500, 1550, 1600, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1462, 1512, 1562, 1612, 570, 620]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # big files unattended removal
    [tc.RemoveFile(60, 'radfet_10'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, 'p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(62, 'p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(63, 'p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(64, 'p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(65, 'p5_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(66, 'p6_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(67, 'p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(68, 'p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(69, 'p9_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(70, 'p10_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(90, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]