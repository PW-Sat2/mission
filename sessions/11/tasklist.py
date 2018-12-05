tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(208, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(1, '/pld_1', [4, 5, 6]), Send, WaitMode.Wait],

    # Wing CAM - mid res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(23, '/pld_1_1.jpg', [i for i in range(0, 6, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/pld_1_1.jpg', [i for i in range(6, 12, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(25, '/pld_1_1.jpg', [i for i in range(12, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/pld_1_1.jpg', [i for i in range(18, 24, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(27, '/pld_1_1.jpg', [i for i in range(24, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/pld_1_1.jpg', [i for i in range(30, 42, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(29, '/pld_1_1.jpg', [i for i in range(42, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/pld_1_1.jpg', [i for i in range(52, 58, 1)]), Send, WaitMode.Wait],

    # telemetry.previous to check state just before and during pld commissioning
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(177, '/telemetry.previous', [i for i in range(1200, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(178, '/telemetry.previous', [i for i in range(1250, 2280, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(179, '/telemetry.previous', [i for i in range(1225, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(180, '/telemetry.previous', [i for i in range(1275, 2280, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(181, '/telemetry.previous', [i for i in range(1212, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/telemetry.previous', [i for i in range(1227, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(183, '/telemetry.previous', [i for i in range(1262, 2280, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/telemetry.previous', [i for i in range(1287, 2280, 100)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(185, '/telemetry.previous', [i for i in range(1000, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/telemetry.previous', [i for i in range(1012, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(187, '/telemetry.previous', [i for i in range(1025, 1800, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(189, '/telemetry.previous', [i for i in range(1037, 1800, 50)]), Send, WaitMode.Wait],
]
