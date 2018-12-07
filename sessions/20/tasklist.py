tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(100, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(121, '/telemetry.current', [i for i in range(1800, 2200, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/telemetry.current', [i for i in range(1850, 2200, 100)]), Send, WaitMode.Wait],

    [tc.SetBitrate(99, 8), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.DownloadFile(124, '/telemetry.current', [i for i in range(1825, 2200, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/telemetry.current', [i for i in range(1875, 2200, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
