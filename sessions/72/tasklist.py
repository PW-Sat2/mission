tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 71 and 72
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(630, 1350, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(680, 1350, 100)]), Send, WaitMode.Wait],

    # Power cycle
    [tc.RawI2C(13, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set periodic
    [tc.SetPeriodicMessageTelecommand(correlation_id=4, interval_minutes=1, repeat_count=1, message='We are the Borg.Lower your shields and surrender your ships.We will add your biological and technological distinctiveness to our own.Resistance is futile'), Send, WaitMode.Wait],
    
    # Persistent state
    [tc.GetPersistentState(), Send, WaitMode.Wait],

    # Set back to 9600
    [[tc.SetBitrate(100, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # More telemetry between session 71 and 72
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(655, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(705, 1350, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(640, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(645, 1350, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(670, 1350, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(715, 1350, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
