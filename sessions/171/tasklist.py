tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 170 and 171
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1270, 1470, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1276, 1470, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 168 and 170
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(6, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(18, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(30, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(42, 1280, 96)]), Send, WaitMode.Wait],

    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(54, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(66, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(78, 1280, 96)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(90, 1280, 96)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]