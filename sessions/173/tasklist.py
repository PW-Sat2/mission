tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 171 and 173
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 250, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1450, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1474, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1462, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1486, 2280, 48)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]