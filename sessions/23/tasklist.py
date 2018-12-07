tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(850, 1100, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(858, 1100, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(866, 1100, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(853, 1100, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(861, 1100, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(869, 1100, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 12], SendLoop, WaitMode.NoWait],
]
