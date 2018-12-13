tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 57 and 58
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(760, 960, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(785, 960, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(5, '/telemetry.current', [i for i in range(772, 960, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/telemetry.current', [i for i in range(797, 960, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(7, '/telemetry.current', [i for i in range(766, 960, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(8, '/telemetry.current', [i for i in range(778, 960, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(9, '/telemetry.current', [i for i in range(791, 960, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(803, 960, 50)]), Send, WaitMode.Wait],

    # High res photos
    [tc.DownloadFile(10, '/p7_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/p7_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/p7_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/p7_480_0', [i for i in range(75, 95, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/p13_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p13_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p13_480_0', [i for i in range(50, 78, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/p12_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p12_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p12_480_0', [i for i in range(50, 77, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(40, '/p11_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p11_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p11_480_0', [i for i in range(50, 76, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/p8_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p8_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p8_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p8_480_0', [i for i in range(75, 83, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p9_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p9_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p9_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/p6_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p6_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p6_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
