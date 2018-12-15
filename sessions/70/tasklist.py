tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 69 and 70
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(290, 550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(296, 550, 12)]), Send, WaitMode.Wait],

    # Missing telemetry between session 67 and 0:00
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1290, 1600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1302, 1600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1296, 1600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1308, 1600, 25)]), Send, WaitMode.Wait],

    # RadFET 2 exp data
    [tc.DownloadFile(16, '/radfet_2', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 0:00 and session 70
    [tc.DownloadFile(17, '/telemetry.previous', [i for i in range(1600, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.previous', [i for i in range(1615, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.previous', [i for i in range(1607, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(1622, 2280, 30)]), Send, WaitMode.Wait],

    # More telemetry between session 68 and 69
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(0, 290, 20)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(10, 290, 20)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(5, 290, 20)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(15, 290, 20)]), Send, WaitMode.Wait],

    # Much much much more telemetry between session 67 and 69
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1453, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1478, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1471, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [i for i in range(1483, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(1489, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(1495, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(1498, 2280, 50)]), Send, WaitMode.Wait],
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
