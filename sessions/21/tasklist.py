tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.SetBitrate(198, 1), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(12, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(221, '/telemetry.previous', [i for i in range(2100, 2280, 20)]), Send, WaitMode.Wait],
    [tc.DownloadFile(223, '/telemetry.previous', [i for i in range(2110, 2280, 20)]), Send, WaitMode.Wait],

    [tc.DownloadFile(225, '/telemetry.current', [i for i in range(0, 30, 5)]), Send, WaitMode.Wait],

    [tc.SetBitrate(199, 8), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
