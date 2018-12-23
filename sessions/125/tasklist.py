tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 124 and 125
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(2070, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(2076, 2250, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(2073, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(2079, 2250, 12)]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(20, '/p1_128_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p2_128_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p3_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p4_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p5_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p6_128_0', [i for i in range(0, 9, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/p7_128_0', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p8_128_0', [i for i in range(0, 7, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p9_128_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p10_128_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 124 and 125
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(2071, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(2072, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(2074, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(2075, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(2077, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(2078, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(2080, 2250, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(2081, 2250, 12)]), Send, WaitMode.Wait],
    

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]