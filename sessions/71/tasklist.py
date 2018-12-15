tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 70 and 71
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(450, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(475, 650, 50)]), Send, WaitMode.Wait],

    # RadFET exp missing chunks
    [tc.DownloadFile(13, '/radfet_2', [10, 12, 13]), Send, WaitMode.Wait],

    # gap between 13-12-2018 20:26 and 20:36
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(1127, 1149, 2)]), Send, WaitMode.Wait],

    # gap between 13-12-2018 20:43 and 20:54
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(1163, 1183, 2)]), Send, WaitMode.Wait],

    # gap between 13-12-2018 21:02 and 21:12
    [tc.DownloadFile(16, '/telemetry.previous', [i for i in range(1199, 1219, 2)]), Send, WaitMode.Wait],

    # gap between 13-12-2018 21:20 and 21:30
    [tc.DownloadFile(17, '/telemetry.previous', [i for i in range(1235, 1255, 2)]), Send, WaitMode.Wait],

    # gap between 13-12-2018 21:38 and 21:49
    [tc.DownloadFile(18, '/telemetry.previous', [i for i in range(1251, 1273, 2)]), Send, WaitMode.Wait],

    # gap between 13-12-2018 21:55 and 22:12
    [tc.DownloadFile(19, '/telemetry.previous', [i for i in range(1305, 1339, 2)]), Send, WaitMode.Wait],

    # More telemetry between session 70 and 71
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(462, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(487, 650, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(456, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(468, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(481, 650, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(493, 650, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
