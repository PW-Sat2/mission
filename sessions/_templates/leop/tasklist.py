tasks = [
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.ListFiles(1, '/'), Send, WaitMode.NoWait],
    [tc.DownloadFile(2, '/telemetry.current', [i for i in range(0, 300, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(3, '/leop', [i for i in range(0, 300, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(4, '/telemetry.leop', [i for i in range(0, 400, 20)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
]
