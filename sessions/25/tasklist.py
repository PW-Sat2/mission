tasks = [
    [[tc.SetBitrate(38, 1), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(32, '/'), Send, WaitMode.Wait],

    # Telemetry between session 24 and now
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1200, 2200, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [i for i in range(1233, 2200, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [i for i in range(1266, 2200, 100)]), Send, WaitMode.Wait],

    [tc.SetBitrate(39, 8), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]
