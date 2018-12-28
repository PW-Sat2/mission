tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # wait for better SNR
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # More telemetry between sessions 148 and 151
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(6, 370, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(1206, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(1212, 2280, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(18, 370, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1218, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1231, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1237, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.previous', [i for i in range(1243, 2280, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]