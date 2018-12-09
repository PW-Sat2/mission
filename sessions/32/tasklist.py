tasks = [
    [[tc.SetBitrate(69, 8), 3], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(250, '/'), Send, WaitMode.Wait],

    # Telemetry between session 30 and 32
    [tc.DownloadFile(25, '/telemetry.previous', [i for i in range(1600, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.previous', [i for i in range(1608, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.previous', [i for i in range(1616, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.previous', [i for i in range(1632, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.previous', [i for i in range(1640, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(0, 600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(8, 600, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(16, 600, 25)]), Send, WaitMode.Wait],

    # SunS experiment data download
    [tc.DownloadFile(46, '/suns_1', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_1', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_1', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_1', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_1', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_1', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_1', [i for i in range(150, 175, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_1', [i for i in range(175, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_1', [i for i in range(200, 225, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_1', [i for i in range(225, 250, 1)]), Send, WaitMode.Wait],

    # Deleting old commissioning files
    [tc.RemoveFile(9, '/cam'), Send, WaitMode.Wait],
    [tc.RemoveFile(10, '/cam_0.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(11, '/cam_1.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(12, '/pld_1_2.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(13, '/suns_test'), Send, WaitMode.Wait],
    [tc.RemoveFile(14, '/suns_test_sec'), Send, WaitMode.Wait],

    [tc.ListFiles(251, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
