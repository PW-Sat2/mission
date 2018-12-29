tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(5), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 161 and 163
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(0, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(25, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [i for i in range(1930, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [i for i in range(1942, 2280, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(12, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(37, 970, 50)]), Send, WaitMode.Wait],

    # Low-res photos just before and after sail deployment
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/sail.photo_31', [12, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/sail.photo_33', [11]), Send, WaitMode.Wait],

    # Low-res photos just before and after sail deployment
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/sail.photo_59', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/sail.photo_59', [i for i in range(15, 29, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/sail.photo_61', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/sail.photo_61', [i for i in range(15, 27, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/sail.photo_63', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/sail.photo_63', [i for i in range(15, 27, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/sail.photo_65', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/sail.photo_65', [i for i in range(15, 27, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/sail.photo_69', [i for i in range(0, 22, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/sail.photo_71', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],

    # Low-res photos just before and after sail deployment
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/sail.photo_73', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/sail.photo_75', [i for i in range(0, 21, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/sail.photo_77', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/sail.photo_77', [i for i in range(15, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/sail.photo_79', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/sail.photo_79', [i for i in range(15, 27, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/sail.photo_81', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/sail.photo_81', [i for i in range(15, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/sail.photo_83', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/sail.photo_83', [i for i in range(16, 33, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/sail.photo_85', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/sail.photo_85', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 161 and 163
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(200, '/telemetry.current', [i for i in range(6, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [i for i in range(18, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [i for i in range(31, 970, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.current', [i for i in range(43, 970, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(204, '/telemetry.previous', [i for i in range(1936, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/telemetry.previous', [i for i in range(1948, 2280, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]