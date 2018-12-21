tasks = [
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(1, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]