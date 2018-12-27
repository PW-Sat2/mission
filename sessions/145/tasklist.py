tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # wait for better SNR
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Telemetry between sessions 144 and 145
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(0, 50, 3)]), Send, WaitMode.Wait],

    # More telemetry between session 142 and 145
    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(856, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [i for i in range(862, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [i for i in range(868, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [i for i in range(877, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.previous', [i for i in range(883, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [i for i in range(889, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.previous', [i for i in range(895, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [i for i in range(904, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [i for i in range(910, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [i for i in range(916, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [i for i in range(922, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.previous', [i for i in range(931, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [i for i in range(937, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.previous', [i for i in range(943, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [i for i in range(949, 2280, 100)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]