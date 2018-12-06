tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(11, '/'), Send, WaitMode.Wait],

    # Pld commissioning photo remove
    [tc.RemoveFile(12, '/pld_1_2.jpg'), Send, WaitMode.Wait],

    # Camera commissioning photos remove
    # Photos cam_0.jpg and cam_1.jpg to be removed later
    [tc.RemoveFile(13, '/cam_2.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(14, '/cam_3.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(15, '/cam_4.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(16, '/cam_5.jpg'), Send, WaitMode.Wait],

    [tc.ListFiles(18, '/'), Send, WaitMode.Wait],

    # Camera commissioning file download to see camera attempts
    [tc.DownloadFile(153, '/cam', [0]), Send, WaitMode.Wait],

    # Not received chunks of suns experiment
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(116, '/suns_test_sec', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/suns_test_sec', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/suns_test_sec', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(117, '/suns_test', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/suns_test', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/suns_test', [i for i in range(50, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/suns_test', [i for i in range(60, 70, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(121, '/suns_test', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/suns_test', [i for i in range(80, 90, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/suns_test', [i for i in range(90, 100, 1)]), Send, WaitMode.Wait],

    # Telemetry when triggered suns experiment
    [tc.DownloadFile(126, '/telemetry.previous', [i for i in range(1900, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.previous', [i for i in range(1912, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/telemetry.previous', [i for i in range(1906, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.previous', [i for i in range(1918, 2280, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(130, '/telemetry.current', [i for i in range(0, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/telemetry.current', [i for i in range(25, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/telemetry.current', [i for i in range(12, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/telemetry.current', [i for i in range(37, 550, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(134, '/telemetry.current', [i for i in range(6, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/telemetry.current', [i for i in range(18, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/telemetry.current', [i for i in range(31, 550, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/telemetry.current', [i for i in range(43, 550, 50)]), Send, WaitMode.Wait],

    # More accurate telemetry around SunS experiment
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(138, '/telemetry.previous', [i for i in range(1903, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/telemetry.previous', [i for i in range(1909, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(140, '/telemetry.previous', [i for i in range(1915, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/telemetry.previous', [i for i in range(1921, 2280, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
]
