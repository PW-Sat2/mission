tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # wait for better SNR
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # Telemetry between sessions 151 and 152
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(380, 580, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(386, 580, 12)]), Send, WaitMode.Wait],

    # More telemetry between sessions 150 and 151 - temperature peak (10:00)
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(203, 380, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(209, 380, 12)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]