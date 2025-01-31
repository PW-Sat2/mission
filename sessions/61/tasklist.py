tasks = [
    [[tc.SetBitrate(98, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(99, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(100, '/p11_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(101, '/p12_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(102, '/p13_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(103, '/p14_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(104, '/p15_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(105, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(106, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(107, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(108, '/p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(109, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(110, '/p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(111, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(112, '/p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(113, '/p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(114, '/p5_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(115, '/p6_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(116, '/p6_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(117, '/p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(118, '/p7_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(119, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(120, '/p8_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(121, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(122, '/p9_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(123, '/suns_2'), Send, WaitMode.Wait],
    [tc.RemoveFile(124, '/suns_2_sec'), Send, WaitMode.Wait],

    [tc.ListFiles(66, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
