tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(218, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(77, '/telemetry.previous', [i for i in range(1950, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.previous', [i for i in range(1962, 2280, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(0, 400, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(12, 400, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(6, 400, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(18, 400, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(224, '/leop', [i for i in range(3, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(225, '/leop', [i for i in range(9, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(226, '/leop', [i for i in range(15, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(227, '/leop', [i for i in range(21, 580, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.PerformCameraCommissioningExperiment(11, 'cam'), Send, WaitMode.Wait],
]
