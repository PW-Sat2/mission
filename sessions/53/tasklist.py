tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 51 and 53
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(12, 600, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(1850, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1862, 2280, 25)]), Send, WaitMode.Wait],

    # SunS experiment download
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(25, '/suns_2', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_2', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/suns_2', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_2', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_2', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/suns_2', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_2', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_2', [i for i in range(175, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_2', [i for i in range(200, 225, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_2', [i for i in range(225, 250, 1)]), Send, WaitMode.Wait],

    # Chunk by chunk telemetry during SunS Experiment
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.previous', [i for i in range(1650, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1651, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1652, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1653, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1654, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1655, 1850, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(46, '/telemetry.previous', [i for i in range(1656, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [i for i in range(1657, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [i for i in range(1658, 1850, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [i for i in range(1659, 1850, 10)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
