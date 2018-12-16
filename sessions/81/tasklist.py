tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 80 and 81
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(1800, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(1806, 2050, 12)]), Send, WaitMode.Wait],

    # Missing chunks of high res photos
    [tc.DownloadFile(11, '/p6_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/p6_480_0', [65, 66, 67, 82, 84, 85, 101, 105, 120, 121, 160, 161]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/p7_480_0', [7, 8, 9, 10, 11, 25, 26, 92, 93, 34, 35, 38, 40, 74]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(14, '/p8_480_0', [24]), Send, WaitMode.NoWait],
    [tc.DownloadFile(15, '/p1_480_0', [10]), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/p5_480_0', [76, 13, 80, 52]), Send, WaitMode.Wait],

    # Fourth SunS Experiment data
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(21, '/suns_4', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/suns_4', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/suns_4', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/suns_4', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/suns_4', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_4', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(27, '/suns_4', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_4', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_4', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_4', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_4', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_4', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_4', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 80 and 81
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1801, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1802, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1803, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1804, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1805, 2050, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1807, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1808, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1809, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(1810, 2050, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(1811, 2050, 12)]), Send, WaitMode.Wait],

    # Much more telemetry between session 78 and 80
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(993, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(999, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(1005, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(1011, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(1018, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(1021, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(1030, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(1033, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(1038, 1800, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(992, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(994, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(997, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(1002, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(1004, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(1007, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [i for i in range(1012, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(1014, 1800, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(1017, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [i for i in range(1022, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(1024, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(1027, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(1022, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(1024, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(1027, 1800, 50)]), Send, WaitMode.Wait],

    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
