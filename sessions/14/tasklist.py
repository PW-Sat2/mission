tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(168, '/'), Send, WaitMode.Wait],

    # Nadir CAM - high res - rest of chunks
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(111, '/pld_1_2.jpg', [5]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(218, '/pld_1_2.jpg', [i for i in range(80, 90, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(219, '/pld_1_2.jpg', [i for i in range(90, 100, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(220, '/pld_1_2.jpg', [i for i in range(100, 110, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(221, '/pld_1_2.jpg', [i for i in range(110, 120, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(222, '/pld_1_2.jpg', [i for i in range(120, 130, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(223, '/pld_1_2.jpg', [i for i in range(130, 140, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(224, '/pld_1_2.jpg', [i for i in range(140, 150, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(225, '/pld_1_2.jpg', [i for i in range(150, 165, 1)]), Send, WaitMode.Wait],

    # telemetry
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(500, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(512, 700, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(506, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(518, 700, 25)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(503, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(509, 700, 25)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(515, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(521, 700, 25)]), Send, WaitMode.Wait],

    # Nadir CAM - low res - sholud be shadowed
    [tc.DownloadFile(226, '/cam_0.jpg', [i for i in range(0, 5, 1)]), Send, WaitMode.Wait],

    # Nadir mid res - same case
    [tc.DownloadFile(227, '/cam_1.jpg', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(118, '/telemetry.current', [i for i in range(500, 1700, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/telemetry.current', [i for i in range(550, 1700, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/telemetry.current', [i for i in range(525, 1700, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/telemetry.current', [i for i in range(575, 1700, 100)]), Send, WaitMode.Wait],
]
