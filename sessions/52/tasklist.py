tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 50 and 52
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1650, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1700, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 600, 100)]), Send, WaitMode.Wait],

    # Read memory to check RAM utilization before power cycle
    [tc.ReadMemory(13, 0x8809ec74, 4), Send, WaitMode.Wait],

    # Power Cycle EPS controller A
    [tc.RawI2C(14, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Read memory to check RAM utilization after power cycle
    [tc.ReadMemory(15, 0x8809ec74, 4), Send, WaitMode.Wait],

    # Goodbye satellite with 9600
    [tc.SetBitrate(16, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],


    # -------- Less important tasks - may be moved to a next session --------
    # More telemetry between session 50 and 52
    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(1466, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.previous', [i for i in range(1482, 2280, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(25, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(12, 600, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(37, 600, 50)]), Send, WaitMode.Wait],

    # SunS experiment download
    [tc.DownloadFile(25, '/suns_2', [i for i in range(0, 25, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_2', [i for i in range(25, 50, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/suns_2', [i for i in range(50, 75, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_2', [i for i in range(75, 100, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_2', [i for i in range(100, 125, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_2', [i for i in range(125, 150, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_2', [i for i in range(150, 175, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_2', [i for i in range(175, 200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_2', [i for i in range(200, 225, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_2', [i for i in range(225, 250, 25)]), Send, WaitMode.Wait],

    # Chunk by chunk telemetry during SunS Experiment
    [tc.DownloadFile(40, '/telemetry.previous', [i for i in range(1650, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1651, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1652, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1653, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1654, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1655, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [i for i in range(1656, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [i for i in range(1657, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [i for i in range(1658, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [i for i in range(1659, 1850, 10)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
