tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # manually-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(370, 550, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(376, 550, 12)]), Send, WaitMode.Wait],
    # manually-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # hi-res focie
    # focia 4 hi-res
    [tc.DownloadFile(60, '/p4_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p4_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p4_480_0', [i for i in range(46, 63, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 7 hi-res
    [tc.DownloadFile(70, '/p7_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p7_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p7_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p7_480_0', [i for i in range(69, 87, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove already downloaded photos
    [tc.RemoveFile(207, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/p10_128_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(210, '/p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/p2_480_0'), Send, WaitMode.Wait],
    
    [tc.ListFiles(212, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]