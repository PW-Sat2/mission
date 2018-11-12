tasks = [
    [tc.PingTelecommand(), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.ListFiles(1, '/'), Send, WaitMode.NoWait],
]
