tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1221, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1227, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [i for i in range(1233, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [i for i in range(1240, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [i for i in range(1247, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [i for i in range(1254, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [i for i in range(1261, 2280, 52)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [i for i in range(1268, 2280, 52)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]