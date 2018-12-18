tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 89 and 90
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1540, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1552, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1546, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1558, 1740, 25)]), Send, WaitMode.Wait],

    # Download missing chunks
    [tc.DownloadFile(20, '/p4_480_0', [22]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p17_480_0', [12, 20, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p18_480_0', [0, 1, 39, 42, 19, 22, 24]), Send, WaitMode.Wait],

    # Remove downloaded res photos
    [tc.RemoveFile(60, '/p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(61, '/p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(62, '/p5_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # More telemetry between session 89 and 90
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1541, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(1542, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(1543, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(1544, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(1545, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(1547, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(1548, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(1549, 1740, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(1550, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(1551, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1553, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1554, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1555, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1556, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1557, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1559, 1740, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1560, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1561, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(1562, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(1563, 1740, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1564, 1740, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
