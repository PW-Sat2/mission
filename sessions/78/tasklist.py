tasks = [
    [[tc.SetBitrate(20, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(21, '/'), Send, WaitMode.Wait],

    # Telemetry between session 77 and 78
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(800, 1015, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(812, 1015, 25)]), Send, WaitMode.Wait],

    # Missing chunks of low res photos
    [tc.DownloadFile(40, '/p8_128_0', [5]), Send, WaitMode.Wait],

    # Few chunks of high res photos - to see if there is something
    [tc.DownloadFile(50, '/p1_480_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p1_480_0', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(53, '/p2_480_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p2_480_0', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p2_480_0', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/p1_480_0', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p1_480_0', [i for i in range(40, 47, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(58, '/p2_480_0', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p2_480_0', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p2_480_0', [i for i in range(50, 54, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 77 and 78
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(806, 1015, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(818, 1015, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(803, 1015, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(809, 1015, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(815, 1015, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(821, 1015, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
