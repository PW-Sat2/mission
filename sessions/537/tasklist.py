tasks = [
    # Generated on 2019-02-24 20:32:51.649000, contains telemetry from sessions 536 to 537.
    # The session starts on 2019-02-24 21:47:34+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1174, 1224, 1274, 1324, 1374, 1199, 1249, 1299, 1349, 1187, 1237, 1287, 1337, 1387, 1211, 1261, 1311, 1361, 1181, 1231]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1281, 1331, 1381, 1193, 1243, 1293, 1343, 1393, 1205, 1255, 1305, 1355, 1217, 1267, 1317, 1367]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missings from previous session
    [tc.DownloadFile(40, '/telemetry.previous', [1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1473, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1823]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.previous', [1835, 1885, 1923, 1935, 1973, 1985, 2023, 2035, 2073, 2085, 2123, 2135, 2173, 2185, 2223, 2235, 2273]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.current', [5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 543, 555, 605, 655, 705, 755, 793]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [805, 843, 855, 893, 905, 943, 955, 993, 1005, 1043, 1055, 1093, 1105, 1143, 1155, 1193, 1205]), Send, WaitMode.Wait],

    # Remove files, trial part
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # [tc.RemoveFile(101, 'p1_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, 'p2_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, 'p3_480_0' ), Send, WaitMode.NoWait],
    # [tc.RemoveFile(104, 'p4_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, 'p5_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, 'p6_480_0' ), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # [tc.RemoveFile(107, 'p7_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, 'p8_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(109, 'p9_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(110, 'p10_480_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait], 

    [tc.ListFiles(112, '/'), Send, WaitMode.Wait],

    # High res photos download
    # 'Chunks': 171, 'File': 'p1_480_0'
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p1_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p1_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p1_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p1_480_0', [i for i in range(129, 155, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p1_480_0', [i for i in range(155, 171, 1)]), Send, WaitMode.Wait],

    # 'Chunks': 169, 'File': 'p7_480_0'
    [tc.DownloadFile(70, '/p7_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p7_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p7_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p7_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p7_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p7_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p7_480_0', [i for i in range(129, 155, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p7_480_0', [i for i in range(155, 169, 1)]), Send, WaitMode.Wait],
 

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]