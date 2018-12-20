tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 101 and 102
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(2070, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(2076, 2270, 12)]), Send, WaitMode.Wait],

    # Photo download
     # Low res photos - few error frames expected
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/p1_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p2_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p3_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p4_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p5_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p6_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(26, '/p7_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p8_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p9_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p10_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 101 and 102
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(2073, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(2079, 2270, 12)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(2071, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(2072, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(2074, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(2075, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(2077, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(2078, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(2080, 2270, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(2081, 2270, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 100 and 101
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(836, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(837, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(839, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(840, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(842, 2150, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(844, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(845, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.current', [i for i in range(847, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.current', [i for i in range(848, 2150, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.current', [i for i in range(849, 2150, 50)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
