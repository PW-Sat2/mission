tasks = [
    # Generated on 2019-06-02 11:29:27.951000, contains telemetry from sessions 1185 to 1186.
    # The session starts on 2019-06-02 12:16:12+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [383, 433, 483, 533, 583, 408, 458, 508, 558, 396, 446, 496, 546, 596, 420, 470, 520, 570, 390, 440]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [490, 540, 590, 402, 452, 502, 552, 602, 414, 464, 514, 564, 426, 476, 526, 576]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.previous', [1399, 1449, 1499, 1549, 1811, 1899, 1911, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [269]), Send, WaitMode.Wait],
    # missing from previous session end


    # file download start
    # SunS experiment data download
    [tc.DownloadFile(46, '/suns_ps_6', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_6', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_6', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_6', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_6', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_6', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_6', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_6', [i for i in range(175, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_6', [i for i in range(200, 225, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_6', [i for i in range(225, 250, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(56, '/suns_ps_6_sec', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_6_sec', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_6_sec', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_6_sec', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_6_sec', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_6_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    # file download end


    # auto-generated file remove start
    [tc.RemoveFile(34, 'p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(35, 'p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(36, 'p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(37, 'p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(38, 'p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(39, 'p6_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(40, 'p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(41, 'p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(42, 'p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(43, 'p10_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(44, 'p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(45, 'p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(46, 'p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(47, 'p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(48, 'p5_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(49, 'p6_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(50, 'p7_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(51, 'p8_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(52, 'p9_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(53, 'p10_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(54, 'radfet_14'), Send, WaitMode.Wait],
    [tc.ListFiles(55, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]