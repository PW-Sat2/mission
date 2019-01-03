tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Telemetry current starting in session 184 and 191
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(0, 1281, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(24, 1281, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(12, 1281, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(36, 1281, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(6, 1281, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(18, 1281, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(30, 1281, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(42, 1281, 48)]), Send, WaitMode.Wait],
    
    [tc.ListFiles(50, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]