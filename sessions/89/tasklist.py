tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 88 and 89
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1350, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1356, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1353, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(1359, 1550, 12)]), Send, WaitMode.Wait],

    # Missing photos of high res photos
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/p2_480_0', [0, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p3_480_0', [1, 2, 3, 26, 71, 75, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p4_480_0', [28, 50, 52, 54, 70, 71, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p5_480_0', [33, 34, 35, 41, 42, 43, 46, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p17_480_0', [10]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p18_480_0', [17]), Send, WaitMode.Wait],

    [tc.DownloadFile(36, '/p3_128_0', [17]), Send, WaitMode.Wait],

    # More telemetry between session 88 and 89
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1351, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1352, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1354, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1355, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1357, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1358, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1360, 1550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1361, 1550, 12)]), Send, WaitMode.Wait],

    # Delete photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(60, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(62, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(63, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(64, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(65, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(66, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(67, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(68, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(69, '/p11_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(70, '/p12_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(71, '/p13_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(72, '/p14_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(73, '/p15_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(74, '/p16_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(75, '/p17_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(76, '/p18_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(77, '/p19_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(78, '/p20_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(79, '/p21_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(80, '/p22_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(81, '/p23_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(82, '/p24_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(83, '/p25_128_0'), Send, WaitMode.NoWait],

    # Old suns exp
    [tc.RemoveFile(84, '/suns_4_sec'), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # Much more telemetry between session 87 and 88
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(51, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(52, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(54, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(55, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(57, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(58, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(59, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [i for i in range(60, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [i for i in range(61, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(99, '/telemetry.current', [i for i in range(63, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [i for i in range(64, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(65, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(66, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(67, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(69, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(70, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(71, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [i for i in range(72, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [i for i in range(73, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(109, '/telemetry.current', [i for i in range(74, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.current', [i for i in range(76, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.current', [i for i in range(77, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.current', [i for i in range(78, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(114, '/telemetry.current', [i for i in range(79, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.current', [i for i in range(82, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.current', [i for i in range(83, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(119, '/telemetry.current', [i for i in range(84, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/telemetry.current', [i for i in range(85, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/telemetry.current', [i for i in range(86, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/telemetry.current', [i for i in range(89, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/telemetry.current', [i for i in range(91, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(125, '/telemetry.current', [i for i in range(92, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.current', [i for i in range(94, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/telemetry.current', [i for i in range(95, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.current', [i for i in range(97, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/telemetry.current', [i for i in range(98, 1500, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/telemetry.current', [i for i in range(99, 1500, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
