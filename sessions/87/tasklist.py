tasks = [
    [[tc.SetBitrate(10, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(11, '/'), Send, WaitMode.Wait],

    # Telemetry between session 86 and 87
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(2200, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(2206, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(14, '/telemetry.current', [i for i in range(0, 120, 6)]), Send, WaitMode.Wait],

    # Low res photos - few error frames expected
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/p1_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p2_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p3_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p4_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p6_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(46, '/p7_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p8_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p9_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p10_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p11_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p12_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p13_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(53, '/p14_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p15_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p16_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p17_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p18_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p19_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p20_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/p21_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p22_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p23_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p24_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p25_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 86 and 87
    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(2203, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [i for i in range(2209, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/telemetry.previous', [i for i in range(2201, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [i for i in range(2202, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.previous', [i for i in range(2204, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [i for i in range(2205, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.previous', [i for i in range(2207, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [i for i in range(2208, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [i for i in range(2210, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [i for i in range(2211, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(200, '/telemetry.current', [i for i in range(1, 120, 6)]), Send, WaitMode.Wait],
    [tc.DownloadFile(201, '/telemetry.current', [i for i in range(2, 120, 6)]), Send, WaitMode.Wait],
    [tc.DownloadFile(202, '/telemetry.current', [i for i in range(3, 120, 6)]), Send, WaitMode.Wait],
    [tc.DownloadFile(203, '/telemetry.current', [i for i in range(4, 120, 6)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/telemetry.current', [i for i in range(5, 120, 6)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
