tasks = [
    [[tc.SetBitrate(30, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(31, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 45 and 46
    [tc.DownloadFile(32, '/telemetry.previous', [i for i in range(1450, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [i for i in range(1500, 2280, 100)]), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(0, 150, 25)]), Send, WaitMode.Wait],

    # Planned power cycle - EPS B due to high uptime (>2d)
    [tc.PowerCycleTelecommand(36), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Goodbye satellite with 9600
    [tc.SetBitrate(37, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # More telemetry between session 45 and 46
    [tc.DownloadFile(38, '/telemetry.previous', [i for i in range(1466, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [i for i in range(1482, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(12, 150, 25)]), Send, WaitMode.Wait],

    # More telemetry over SAA
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1756, 2100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1768, 2100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1774, 2100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1792, 2100, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
