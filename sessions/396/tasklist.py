tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(200, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p5_128_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(205, '/p6_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(206, '/p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(207, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/p10_128_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(210, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/p5_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(213, '/p8_480_0'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(214, '/suns_ps_1'), Send, WaitMode.Wait],
    [tc.RemoveFile(215, '/suns_ps_1_sec'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]