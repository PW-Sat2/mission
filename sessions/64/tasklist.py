tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 63 and 64
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(90, 290, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(102, 290, 25)]), Send, WaitMode.Wait],

    # Some missing chunks
    [tc.DownloadFile(5, '/p7_128_0', [5]), Send, WaitMode.Wait],
    [tc.DownloadFile(6, '/p9_128_0', [6]), Send, WaitMode.Wait],

    # Remove photos
    [tc.RemoveFile(100, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(200, '/p1_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(101, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(102, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(103, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(104, '/p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(105, '/p6_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(205, '/p6_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(106, '/p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(206, '/p7_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(107, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(207, '/p8_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(108, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(109, '/p10_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/p10_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(110, '/p11_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(210, '/p11_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(111, '/p12_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/p12_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(112, '/p13_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/p13_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(113, '/p14_128_0'), Send, WaitMode.Wait],
    # [tc.RemoveFile(213, '/p14_480_0'), Send, WaitMode.Wait], # pink sun 1

    [tc.RemoveFile(114, '/p15_128_0'), Send, WaitMode.Wait],
    # [tc.RemoveFile(214, '/p15_480_0'), Send, WaitMode.Wait], # pink sun 2

    [tc.RemoveFile(115, '/p16_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(215, '/p16_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(116, '/p17_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(216, '/p17_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(117, '/p18_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(217, '/p18_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(118, '/p19_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(218, '/p19_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(119, '/p20_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(219, '/p20_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(66, '/'), Send, WaitMode.Wait],

    # Hi res photos
    [tc.DownloadFile(220, '/p14_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(221, '/p14_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(222, '/p14_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(223, '/p14_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(224, '/p14_480_0', [i for i in range(80, 104, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(225, '/p15_480_0', [i for i in range(0, 22, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(226, '/p15_480_0', [i for i in range(22, 44, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(227, '/p15_480_0', [i for i in range(44, 66, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(228, '/p15_480_0', [i for i in range(66, 88, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
