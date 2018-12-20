tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(6, '/'), Send, WaitMode.Wait],

    # Fifth RadFET Experiment
    [tc.PerformRadFETExperiment(7, 150, 110, 'radfet_5'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry between session 102 and 105
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(0, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(25, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(12, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.current', [i for i in range(37, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/telemetry.current', [i for i in range(6, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/telemetry.current', [i for i in range(18, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/telemetry.current', [i for i in range(31, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(19, '/telemetry.current', [i for i in range(43, 1025, 50)]), Send, WaitMode.Wait],

    # Remove files
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/p1_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(102, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/p2_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(104, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, '/p3_480_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(106, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(107, '/p4_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(108, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(109, '/p5_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(110, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(111, '/p6_480_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(112, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(113, '/p7_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(114, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(115, '/p8_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(116, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(117, '/p9_480_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(118, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(119, '/p10_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(120, '/suns_6'), Send, WaitMode.NoWait],
    [tc.RemoveFile(121, '/suns_6_sec'), Send, WaitMode.NoWait],

    # More telemetry between session 102 and 105
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(3, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(9, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(15, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(21, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(28, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(30, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(34, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(40, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [i for i in range(46, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.current', [i for i in range(49, 1025, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(1, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(2, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(4, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(5, 1025, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(7, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(8, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(10, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(11, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(13, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(14, 1025, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(16, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(17, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(19, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(20, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(22, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(23, 1025, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(24, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(26, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(27, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(29, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(32, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(35, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(36, 1025, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(38, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(39, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(40, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(41, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(44, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(45, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [i for i in range(47, 1025, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(48, 1025, 50)]), Send, WaitMode.Wait],
]