tasks = [
    [[tc.SetBitrate(98, 8), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(42, '/'), Send, WaitMode.Wait],

    # Telemetry between session 22 and 23 (more data points)
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(0, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(25, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [i for i in range(12, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', [i for i in range(37, 1000, 50)]), Send, WaitMode.Wait],

    # Telemetry between session 24 and 25 (more data points)
    [tc.DownloadFile(65, '/telemetry.previous', [i for i in range(1200, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.previous', [i for i in range(1225, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.previous', [i for i in range(1212, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.previous', [i for i in range(1237, 2280, 50)]), Send, WaitMode.Wait],

    # Telemetry between session 25 and 26
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(0, 250, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(8, 250, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(16, 250, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]
