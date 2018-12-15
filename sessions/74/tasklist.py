tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Set periodic
    [tc.SetPeriodicMessageTelecommand(correlation_id=5, interval_minutes=1, repeat_count=0, message='empty'), Send, WaitMode.Wait],

    # Telemetry between session 73 and 74
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1450, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1456, 1700, 12)]), Send, WaitMode.Wait],

    # More telemetry
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1451, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1452, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1453, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1454, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1455, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1457, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(1458, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(1459, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(1460, 1700, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(1461, 1700, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
