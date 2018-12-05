tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [tc.PerformPayloadCommissioningExperiment(70, 'pld_1'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(155, '/telemetry.current', [i for i in range(100, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(161, '/telemetry.current', [i for i in range(3, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(157, '/telemetry.current', [i for i in range(4, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(158, '/telemetry.current', [i for i in range(6, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(159, '/telemetry.current', [i for i in range(8, 200, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(160, '/telemetry.current', [i for i in range(9, 200, 10)]), Send, WaitMode.Wait],

    [tc.ListFiles(201, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(120, '/leop', [i for i in range(6, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(121, '/leop', [i for i in range(18, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(122, '/leop', [i for i in range(31, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(123, '/leop', [i for i in range(43, 580, 50)]), Send, WaitMode.Wait],

    [tc.ListFiles(202, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(124, '/leop', [i for i in range(3, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(125, '/leop', [i for i in range(9, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(126, '/leop', [i for i in range(15, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(127, '/leop', [i for i in range(21, 580, 50)]), Send, WaitMode.Wait],

    [tc.ListFiles(203, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(128, '/leop', [i for i in range(28, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(129, '/leop', [i for i in range(34, 580, 50)]), Send, WaitMode.Wait],

    [tc.ListFiles(204, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(130, '/leop', [i for i in range(40, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(131, '/leop', [i for i in range(46, 580, 50)]), Send, WaitMode.Wait],
]
