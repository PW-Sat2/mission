tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(7, '/'), Send, WaitMode.Wait],

    # Telemetry between session 183 and 184
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(900, 1100, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(906, 1100, 12)]), Send, WaitMode.Wait],

    # High res photos missings
    [tc.DownloadFile(20, '/p1_480_0', [57,71,73]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/p2_480_0', [1]), Send, WaitMode.Wait],

    # High res photos download
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/p7_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p7_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p7_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p7_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(34, '/p7_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p7_480_0', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p7_480_0', [i for i in range(120, 146, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p9_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(41, '/p9_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p9_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p9_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p9_480_0', [i for i in range(80, 101, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]