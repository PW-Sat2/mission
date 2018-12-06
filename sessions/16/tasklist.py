tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Nadir CAM - high res - last chunks downloading
    [tc.DownloadFile(9, '/pld_1_2.jpg', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],

    # Deleting first pld commissioning files
    [tc.RemoveFile(11, '/pld_1_0.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(12, '/pld_1_1.jpg'), Send, WaitMode.Wait],
    # Not fully downloaded pld_1_2.jpg so skipped here
    [tc.RemoveFile(13, '/pld_1_3.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(14, '/pld_1_4.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(15, '/pld_1_5.jpg'), Send, WaitMode.Wait],
    [tc.RemoveFile(16, '/pld_1'), Send, WaitMode.Wait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # Deleting leop
    [tc.RemoveFile(21, '/leop'), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Persisten state
    [tc.GetPersistentState(), Send, WaitMode.Wait],

    # Downloading SunS Experiment data
    [tc.DownloadFile(111, '/suns_test', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/suns_test', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/suns_test', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(114, '/suns_test_sec', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/suns_test_sec', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/suns_test_sec', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],

    # Dark photos from camera commissioning
    [tc.DownloadFile(176, 'cam_0.jpg', [0]), Send, WaitMode.Wait],
    [tc.DownloadFile(177, 'cam_1.jpg', [0, 1, 8]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(117, '/suns_test', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/suns_test', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/suns_test', [i for i in range(50, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/suns_test', [i for i in range(60, 70, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(121, '/suns_test', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/suns_test', [i for i in range(80, 90, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/suns_test', [i for i in range(90, 100, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(124, '/suns_test_sec', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/suns_test_sec', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],

    # Telemetry when triggered suns experiment
    [tc.DownloadFile(126, '/telemetry.previous', [i for i in range(1900, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.previous', [i for i in range(1912, 2280, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(128, '/telemetry.previous', [i for i in range(1906, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.previous', [i for i in range(1909, 2280, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
]
