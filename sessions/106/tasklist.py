tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 105 and 106
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1000, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1006, 1200, 12)]), Send, WaitMode.Wait],

    # RadFET exp data
    [tc.DownloadFile(20, '/radfet_5', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    # Remove files
    [tc.RemoveFile(30, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(31, '/p2_128_0'), Send, WaitMode.Wait],

    # More telemetry between session 105 and 106
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1003, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1009, 1200, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1001, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1002, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1004, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1005, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1007, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1008, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(1010, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(1011, 1200, 12)]), Send, WaitMode.Wait],
]