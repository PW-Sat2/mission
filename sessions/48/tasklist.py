tasks = [
    [[tc.SetBitrate(50, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(51, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 47 and 48
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(200, 400, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(225, 400, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(212, 400, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(237, 400, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(206, 400, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(218, 400, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(232, 400, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(243, 400, 50)]), Send, WaitMode.Wait],

    # Photos
    [tc.DownloadFile(60, '/hor_0', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/hor_0', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/hor_5', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/hor_5', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/hor_10', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/hor_10', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/hor_15', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/hor_15', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(68, '/hor_20', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/hor_20', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/hor_25', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/hor_25', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
