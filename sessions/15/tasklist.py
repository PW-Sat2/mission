tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(170, '/'), Send, WaitMode.Wait],

    [tc.PerformSunSExperiment(113, 0, 20, 10, datetime.timedelta(seconds=5), 30, datetime.timedelta(minutes=4), 'suns_test'), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(1600, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(1602, 1800, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(1604, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(1608, 1800, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(1610, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(1612, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [i for i in range(1614, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [i for i in range(1616, 1800, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(109, '/telemetry.current', [i for i in range(1618, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.current', [i for i in range(1620, 1800, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [i for i in range(1622, 1800, 25)]), Send, WaitMode.Wait],
]
