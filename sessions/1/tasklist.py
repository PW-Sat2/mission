tasks = [
    [tc.PingTelecommand(), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.ListFiles(1, '/'), Send, WaitMode.NoWait],
]
