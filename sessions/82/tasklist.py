tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 81 and 82
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(0, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(25, 1100, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(5, '/telemetry.previous', [i for i in range(2000, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.previous', [i for i in range(2006, 2280, 12)]), Send, WaitMode.Wait],


    # Third RadFET experiment
    [tc.PerformRadFETExperiment(7, 150, 110, 'radfet_3'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],


    # Missing chunks of high res photos
    [tc.DownloadFile(11, '/p6_480_0', [0, 1, 6, 7]), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/p7_480_0', [35]), Send, WaitMode.Wait],

    # Delete downloaded low photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(20, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(21, '/p2_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(22, '/p3_128_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(23, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(24, '/p4_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(25, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(26, '/p5_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(27, '/p6_128_0'), Send, WaitMode.NoWait],
    # p6_480_0 not downloaded yet

    [tc.RemoveFile(28, '/p7_128_0'), Send, WaitMode.Wait],
    # p7_480_0 not downloaded yet

    [tc.RemoveFile(29, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(30, '/p8_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(31, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(32, '/p9_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(33, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(34, '/p10_480_0'), Send, WaitMode.NoWait],

    [tc.RemoveFile(35, '/p12_128_0'), Send, WaitMode.NoWait],
    # p12_480_0 - to be removed - overexposed Earth

    [tc.RemoveFile(36, '/p13_128_0'), Send, WaitMode.NoWait],
    # p13_480_0 - to be removed - overexposed Earth

    [tc.RemoveFile(37, '/p14_128_0'), Send, WaitMode.Wait],
    # p14_480_0 - to be removed - Sun or overexposed Earth

    [tc.RemoveFile(38, '/p15_128_0'), Send, WaitMode.NoWait],
    # p15_480_0 - to be removed - Sun

    [tc.RemoveFile(39, '/p16_128_0'), Send, WaitMode.NoWait],
    # p16_480_0 - to be removed - Sun

    [tc.RemoveFile(40, '/p17_128_0'), Send, WaitMode.NoWait],
    # p17_480_0 - to be removed - Sun

    [tc.RemoveFile(41, '/p18_128_0'), Send, WaitMode.NoWait],
    # p18_480_0 - to be removed - Sun

    [tc.RemoveFile(42, '/p19_128_0'), Send, WaitMode.NoWait],
    # p19_480_0 - to be removed - Sun

    # p20_128_0 and p20_480_0 - to be removed - Sun

    [tc.ListFiles(49, '/'), Send, WaitMode.Wait],

    # Fourth SunS Experiment secondary data
    [tc.DownloadFile(50, '/suns_4_sec', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_4_sec', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_4_sec', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_4_sec', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_4_sec', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_4_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
 
    # More telemetry between session 81 and 82
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(6, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(12, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(18, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(31, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(37, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(43, 1100, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/telemetry.previous', [i for i in range(2001, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.previous', [i for i in range(2002, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.previous', [i for i in range(2003, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.previous', [i for i in range(2004, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.previous', [i for i in range(2005, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.previous', [i for i in range(2007, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.previous', [i for i in range(2008, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.previous', [i for i in range(2009, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.previous', [i for i in range(2010, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.previous', [i for i in range(2011, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(3, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(9, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [i for i in range(15, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/telemetry.current', [i for i in range(21, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.current', [i for i in range(28, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [i for i in range(34, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [i for i in range(40, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [i for i in range(46, 1100, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/telemetry.current', [i for i in range(48, 1100, 50)]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
