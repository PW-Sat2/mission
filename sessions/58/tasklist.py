tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(0, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(25, 1000, 50)]), Send, WaitMode.Wait],

    # Low res photos - PhotoSuccessFrames received
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/p2_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p10_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p11_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p12_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p13_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p15_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/p16_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p17_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p18_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/p19_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p20_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More telemetry
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(12, 1000, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(37, 1000, 50)]), Send, WaitMode.Wait],

    # Telemetry between session 56 and 57
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/telemetry.previous', [i for i in range(2000, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.previous', [i for i in range(2006, 2280, 12)]), Send, WaitMode.Wait],

    # Much more telemetry between session 53 and 00:00
    [tc.DownloadFile(14, '/telemetry.previous', [i for i in range(580, 980, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/telemetry.previous', [i for i in range(592, 980, 25)]), Send, WaitMode.Wait],

    # Telemetry around photos
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1850, 1870, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1870, 1890, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1890, 1910, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [i for i in range(1910, 1930, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(1930, 1950, 1)]), Send, WaitMode.Wait],

    # SunS 2 secondary file
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/telemetry.previous', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.previous', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.previous', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
