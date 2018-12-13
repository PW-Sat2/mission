tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 55 and 56
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1850, 2050, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(1862, 2050, 25)]), Send, WaitMode.Wait],

    # Telemetry between session 54 and 55
    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(750, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(775, 1850, 50)]), Send, WaitMode.Wait],

    # Low res photos - PhotoSuccessFrames received
    [tc.DownloadFile(20, '/p2_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p5_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p8_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p14_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p15_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 54 and 55
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(762, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(787, 1850, 50)]), Send, WaitMode.Wait],

    # Low res photos - no PhotoSuccessFrames received (error frames expected)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/p0_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(42, '/p3_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p4_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p6_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p7_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(47, '/p9_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p10_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p11_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p12_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p13_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p16_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p17_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p18_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p19_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p20_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # Much more telemetry between session 54 and 55
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(756, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(768, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(781, 1850, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(793, 1850, 50)]), Send, WaitMode.Wait],

    # Much more telemetry between session 55 and 56
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(1856, 2050, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(1868, 2050, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
