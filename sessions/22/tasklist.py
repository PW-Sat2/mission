tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.SetBitrate(18, 1), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(0, 800, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(33, 800, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(66, 800, 100)]), Send, WaitMode.Wait],

    [tc.SetBitrate(19, 8), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],
]
