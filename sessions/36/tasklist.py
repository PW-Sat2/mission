tasks = [
    [[tc.SetBitrate(2, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(1, '/'), Send, WaitMode.Wait],

    # Telemetry between session 35 and 36
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1750, 1950, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1762, 1950, 25)]), Send, WaitMode.Wait],

    [tc.SetBitrate(3, 8), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
