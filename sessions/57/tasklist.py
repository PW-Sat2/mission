tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 56 and 57
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(2000, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(2006, 2280, 12)]), Send, WaitMode.Wait],
    # In case of error frames
    [tc.DownloadFile(5, '/telemetry.previous', [i for i in range(2000, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.previous', [i for i in range(2006, 2280, 12)]), Send, WaitMode.Wait],

    # Much more telemetry between session 53 and 00:00
    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(580, 980, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(592, 980, 25)]), Send, WaitMode.Wait],
    # In case of error frames
    [tc.DownloadFile(9, '/telemetry.previous', [i for i in range(580, 980, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(10, '/telemetry.previous', [i for i in range(592, 980, 25)]), Send, WaitMode.Wait],

    # Low res photos - PhotoSuccessFrames received
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

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
