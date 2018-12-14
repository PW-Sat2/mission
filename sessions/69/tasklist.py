tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 67 and 69
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(12, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1450, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1475, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1462, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1487, 2280, 50)]), Send, WaitMode.Wait],

    # Remove suns sec exp file
    [tc.RemoveFile(20, '/suns_3_sec'), Send, WaitMode.Wait],
    [tc.ListFiles(21, '/'), Send, WaitMode.Wait],

    # RadFet experiment
    [tc.PerformRadFETExperiment(30, 150, 110, 'radfet_2'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # More telemetry between session 67 and 69
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(6, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(18, 370, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1456, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1481, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1468, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1493, 2280, 50)]), Send, WaitMode.Wait],

    # Much much more telemetry between session 67 and 69
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(3, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(9, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(15, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(21, 370, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1453, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1478, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1471, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [i for i in range(1483, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(1489, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(1495, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(1498, 2280, 50)]), Send, WaitMode.Wait],

    # Much much much more telemetry between session 67 and 69
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(1, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(2, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(4, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(5, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(7, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(8, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [i for i in range(10, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(11, 370, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(13, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [i for i in range(14, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(16, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(17, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(19, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(20, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(22, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(23, 370, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(24, 370, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(80, '/telemetry.previous', [i for i in range(1451, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.previous', [i for i in range(1458, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.previous', [i for i in range(1454, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.previous', [i for i in range(1462, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.previous', [i for i in range(1466, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.previous', [i for i in range(1470, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.previous', [i for i in range(1473, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(87, '/telemetry.previous', [i for i in range(1476, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.previous', [i for i in range(1482, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.previous', [i for i in range(1486, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.previous', [i for i in range(1490, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.previous', [i for i in range(1494, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.previous', [i for i in range(1497, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.previous', [i for i in range(1499, 2280, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
