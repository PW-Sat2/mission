tasks = [
    [[tc.SetBitrate(19, 1), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(252, '/'), Send, WaitMode.Wait],

    # Telemetry between session 27 and 29
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(1400, 1600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(1412, 1600, 25)]), Send, WaitMode.Wait],

    [[tc.SetBitrate(17, 8), 3], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
