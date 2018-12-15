tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 70 and 71
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(450, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(475, 650, 50)]), Send, WaitMode.Wait],

    # RadFET exp missing chunks
    [tc.DownloadFile(13, '/radfet_2', [10, 12, 13]), Send, WaitMode.Wait],

    # More telemetry between session 70 and 71
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(462, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(487, 650, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(456, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(468, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(481, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(493, 650, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
