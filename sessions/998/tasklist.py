tasks = [
    # Generated on 2019-04-05 21:21:02.361000, contains telemetry from sessions 997 to 998.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["The next step is telemetry download.", Print, WaitMode.Wait],

    # manually-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', range(0, 150, 6)), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', range(2, 150, 6)), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(99, '/p1_128_0', [35]), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/p2_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(18, 30, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p3_128_0', [i for i in range(18, 32, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p4_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(106, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p5_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(108, '/p6_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p6_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p7_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p7_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(112, '/p8_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p8_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(114, '/p9_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p9_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(116, '/p10_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/p10_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]