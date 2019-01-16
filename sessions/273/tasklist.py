tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(60, '/p1_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p2_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p2_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/p3_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p3_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p4_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p5_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    # add telemetry

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]