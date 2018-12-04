tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(1, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(31, '/leop'), Send, WaitMode.Wait],
    [tc.RemoveFile(32, '/telemetry.leop'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(0, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(50, 1200, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(25, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(75, 1200, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(12, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(37, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(62, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(87, 1200, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(6, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(18, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(31, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(43, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(56, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(68, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(81, 1200, 100)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(93, 1200, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(0, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(5, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(2, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(7, 200, 10)]), Send, WaitMode.Wait],
]
