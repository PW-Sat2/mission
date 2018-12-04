tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],

    [tc.SetBitrate(100, 1), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.leop', [i for i in range(3, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(31, '/telemetry.leop', [i for i in range(9, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(32, '/telemetry.leop', [i for i in range(15, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(33, '/telemetry.leop', [i for i in range(21, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(34, '/telemetry.leop', [i for i in range(28, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(110, '/telemetry.leop', [i for i in range(34, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(35, '/telemetry.leop', [i for i in range(40, 450, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(37, '/telemetry.leop', [i for i in range(46, 450, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/leop', [i for i in range(0, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(21, '/leop', [i for i in range(25, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(22, '/leop', [i for i in range(12, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(23, '/leop', [i for i in range(37, 580, 50)]), Send, WaitMode.Wait],
]
