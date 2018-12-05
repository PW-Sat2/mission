tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(158, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/cam', [i for i in range(0, 2, 1)]), Send, WaitMode.Wait],

    # Wing CAM - low res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(111, '/cam_0.jpg', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(211, '/cam_0.jpg', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    # Nadir CAM - low res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(112, '/cam_3.jpg', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(312, '/cam_3.jpg', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],

    # Wing CAM - mid res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(114, '/cam_1.jpg', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(115, '/cam_1.jpg', [i for i in range(15, 30, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(116, '/cam_1.jpg', [i for i in range(30, 45, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(117, '/cam_1.jpg', [i for i in range(45, 60, 1)]), Send, WaitMode.Wait],

    # Nadir CAM - mid res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(17, '/cam_4.jpg', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(18, '/cam_4.jpg', [i for i in range(10, 25, 1)]), Send, WaitMode.Wait],

    # telemetry
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(500, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(512, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(506, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(518, 700, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(503, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(509, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(515, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(521, 700, 25)]), Send, WaitMode.Wait],
]
