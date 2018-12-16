tasks = [
    [[tc.SetBitrate(3, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PowerCycleTelecommand(2), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(1, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between session 78 and 79
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(990, 1720, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(1015, 1720, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(1002, 1720, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(1027, 1720, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(9, '/telemetry.current', [i for i in range(996, 1720, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1008, 1720, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1024, 1720, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1035, 1720, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
