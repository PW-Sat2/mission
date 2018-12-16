tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 79 and 80
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(1670, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(1675, 1870, 10)]), Send, WaitMode.Wait],

    # Fourth SunS experiment
    [tc.PerformSunSExperiment(6, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_4'), Send, WaitMode.Wait],
    
    # High res photos download
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/p6_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/p6_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/p6_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/p6_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(14, '/p6_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(15, '/p6_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(16, '/p6_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(17, '/p6_480_0', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(18, '/p6_480_0', [i for i in range(160, 171, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/p7_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p7_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p7_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p7_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p7_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p7_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/p7_480_0', [i for i in range(120, 126, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/p5_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p5_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p5_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p5_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p5_480_0', [i for i in range(100, 122, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/p10_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p10_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p10_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p10_480_0', [i for i in range(60, 84, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/p4_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p4_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p4_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p4_480_0', [i for i in range(60, 75, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/p9_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p9_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p9_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p9_480_0', [i for i in range(60, 72, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/p8_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p8_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p8_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p8_480_0', [i for i in range(60, 77, 1)]), Send, WaitMode.Wait],

    # Missing chunks of p1 and p2
    [tc.DownloadFile(80, '/p1_480_0', [10, 25, 27, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p2_480_0', [1, 3, 24, 26, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 47, 48, 49, 51, 52, 53]), Send, WaitMode.Wait],

    # More telemetry between session 79 and 80
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(1671, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(1672, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(1673, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(1674, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(1676, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(1677, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(1678, 1870, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [i for i in range(1679, 1870, 10)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
