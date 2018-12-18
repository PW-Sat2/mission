tasks = [
    [[tc.SetBitrate(3, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between sessions 92 and 93
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(260, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(261, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(262, 452, 10)]), Send, WaitMode.Wait],

    # Fifth SunS Experiment data
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(21, '/suns_5', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/suns_5', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/suns_5', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/suns_5', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/suns_5', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_5', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/suns_5', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_5', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_5', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_5', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_5', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_5', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_5', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    # Delete photos - two times
    [tc.RemoveFile(30, '/p10_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(31, '/p11_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(32, '/p12_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(33, '/p13_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(34, '/p14_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(35, '/p15_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(36, '/p16_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(37, '/p17_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(38, '/p18_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(39, '/p19_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(40, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/p20_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, '/p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(44, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(45, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(46, '/p10_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(47, '/p11_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(48, '/p12_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(49, '/p13_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(50, '/p14_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(51, '/p15_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(52, '/p16_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(53, '/p17_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(54, '/p18_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(55, '/p19_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(56, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(57, '/p20_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(58, '/p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(59, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(60, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(70, '/'), Send, WaitMode.Wait],

    # More telemetry between sessions 92 and 93
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(263, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(264, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(265, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(266, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(267, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(268, 452, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(269, 452, 10)]), Send, WaitMode.Wait],

    # Fifth SunS Experiment secondary data
    [tc.DownloadFile(200, '/suns_5_sec', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/suns_5_sec', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/suns_5_sec', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/suns_5_sec', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/suns_5_sec', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/suns_5_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
