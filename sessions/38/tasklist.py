tasks = [
    [[tc.SetBitrate(73, 8), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(43, '/'), Send, WaitMode.Wait],

    # Telemetry between session 36 and 38
    [tc.DownloadFile(21, '/telemetry.previous', [i for i in range(1958, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.previous', [i for i in range(1966, 2280, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(8, 950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(16, 950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(24, 950, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(32, 950, 50)]), Send, WaitMode.Wait],

    # Low res photo download
    [tc.DownloadFile(101, '/p1_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p2_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p3_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(104, '/p4_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p5_128_0', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
