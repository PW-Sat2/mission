tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PowerCycleTelecommand(2), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(3, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between session 84 and 85
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1350, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1362, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1356, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1368, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(1353, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(1359, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(1365, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(1371, 2200, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
