tasks = [
    [[tc.SetBitrate(80, 1), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(81, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(82, '/p1_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(83, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(84, '/p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(85, '/p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(86, '/p3_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(87, '/p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(88, '/p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(89, '/p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(90, '/p5_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(91, '/suns_1'), Send, WaitMode.Wait],
    [tc.RemoveFile(92, '/suns_1_sec'), Send, WaitMode.Wait],

    [tc.ListFiles(, '/'), Send, WaitMode.Wait],

    # Telemetry between session 41 and 42
    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(2125, 2280, 15)]), Send, WaitMode.Wait],

    # Telemetry between session 41 and 42
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(0, 40, 4)]), Send, WaitMode.Wait],

    # Beacon for goodbye
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SetBitrate(102, 8), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
