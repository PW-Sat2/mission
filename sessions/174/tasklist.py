tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 173 and 174
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(250, 450, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(256, 450, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 171 and 173
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(6, 250, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(1456, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1468, 2280, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1480, 2280, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1492, 2280, 48)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]