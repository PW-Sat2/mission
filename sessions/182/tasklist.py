tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 181 and 182
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(1990, 2250, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(2002, 2250, 24)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(1996, 2250, 24)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(2018, 2250, 24)]), Send, WaitMode.Wait],

    # High res photos download
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(20, '/p4_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p4_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/p4_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/p4_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/p4_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/p4_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/p4_480_0', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/p4_480_0', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/p4_480_0', [i for i in range(160, 171, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p5_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p5_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p5_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p5_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p5_480_0', [i for i in range(100, 111, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p6_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p6_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p6_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p6_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p6_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p6_480_0', [i for i in range(100, 116, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
