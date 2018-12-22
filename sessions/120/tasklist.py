tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 118 and 120
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1700, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.previous', [i for i in range(0, 800, 50)]), Send, WaitMode.Wait],

    # Remove photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(40, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(44, '/p5_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(45, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(46, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(47, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(48, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(49, '/p10_128_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(50, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(51, '/p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(52, '/p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(53, '/p4_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(54, '/p5_480_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(55, '/p6_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(56, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(57, '/p8_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(58, '/p9_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(59, '/p10_480_0'), Send, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(60, '/suns_7'), Send, WaitMode.NoWait],
    [tc.RemoveFile(61, '/suns_7_sec'), Send, WaitMode.NoWait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # More telemetry between session 118 and 120
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(1725, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [i for i in range(25, 800, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(1712, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(1737, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [i for i in range(12, 800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [i for i in range(37, 800, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]