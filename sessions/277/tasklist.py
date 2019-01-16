tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1217, 1267, 1317, 1367, 1417, 1242, 1292, 1342, 1392, 1230, 1280, 1330, 1380, 1430, 1254, 1304, 1354, 1404, 1224, 1274]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1324, 1374, 1424, 1236, 1286, 1336, 1386, 1436, 1248, 1298, 1348, 1398, 1260, 1310, 1360, 1410]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 1 hi-res
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p1_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p1_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p1_480_0', [i for i in range(92, 115, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_480_0', [i for i in range(115, 138, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p1_480_0', [i for i in range(138, 162, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 4 hi-res
    [tc.DownloadFile(70, '/p4_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p4_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p4_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p4_480_0', [i for i in range(69, 75, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 5 hi-res
    [tc.DownloadFile(80, '/p5_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p5_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p5_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p5_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p5_480_0', [i for i in range(92, 115, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p5_480_0', [i for i in range(115, 138, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p5_480_0', [i for i in range(138, 161, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/p5_480_0', [i for i in range(161, 171, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    # focia 3 hi-res
    [tc.DownloadFile(90, '/p3_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/p3_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/p3_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/p3_480_0', [i for i in range(69, 76, 1)]), Send, WaitMode.Wait],

    # Remove already downloaded small photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(200, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_128_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]