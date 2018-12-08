tasks = [
    [[tc.SetBitrate(29, 1), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(155, '/'), Send, WaitMode.Wait],

    # Telemetry between session 30 and 31
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1600, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(0, 400, 50)]), Send, WaitMode.Wait],

    [tc.PerformSunSExperiment(114, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_1'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SetBitrate(27, 8), 3], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
