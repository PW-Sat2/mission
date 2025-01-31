tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(158, '/'), Send, WaitMode.Wait],

    # Nadir CAM - high res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(111, '/pld_1_2.jpg', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(211, '/pld_1_2.jpg', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(212, '/pld_1_2.jpg', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(213, '/pld_1_2.jpg', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(214, '/pld_1_2.jpg', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(215, '/pld_1_2.jpg', [i for i in range(50, 60, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(216, '/pld_1_2.jpg', [i for i in range(60, 70, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(217, '/pld_1_2.jpg', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],
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
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(506, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(518, 700, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(503, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(509, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(515, 700, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(521, 700, 25)]), Send, WaitMode.Wait],
]
