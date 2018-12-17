tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 84 and 85
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(1350, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(1362, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(1356, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(1368, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(1353, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(1359, 2200, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(9, '/telemetry.current', [i for i in range(1365, 2200, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1371, 2200, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
