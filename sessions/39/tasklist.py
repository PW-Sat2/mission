tasks = [
    [[tc.SetBitrate(23, 1), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # Telemetry between session 38 and 39
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(950, 1150, 25)]), Send, WaitMode.Wait],

    # High res photo download
    [tc.DownloadFile(201, '/p4_480_0', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(202, '/p4_480_0', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],

    [[tc.SetBitrate(13, 8), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(203, '/p4_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(204, '/p4_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(205, '/p4_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(206, '/p4_480_0', [i for i in range(80, 93, 1)]), Send, WaitMode.Wait],

    # Second High Res photo
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(210, '/p5_480_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(211, '/p5_480_0', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(212, '/p5_480_0', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(213, '/p5_480_0', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(214, '/p5_480_0', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(215, '/p5_480_0', [i for i in range(125, 135, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
