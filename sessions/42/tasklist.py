tasks = [
    [[tc.SetBitrate(80, 1), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(81, '/'), Send, WaitMode.Wait],

    # Telemetry between session 41 and 42
    [tc.DownloadFile(90, '/telemetry.previous', [i for i in range(2125, 2280, 15)]), Send, WaitMode.Wait],

    # Telemetry between session 41 and 42
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(0, 40, 4)]), Send, WaitMode.Wait],

    # Beacon for goodbye
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SetBitrate(92, 8), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
