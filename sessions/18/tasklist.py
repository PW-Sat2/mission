tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(450, 820, 50)]), Send, WaitMode.Wait],

    [tc.PowerCycleTelecommand(66), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(475, 820, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
]
