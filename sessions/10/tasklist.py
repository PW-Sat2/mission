tasks = [
    [[tc.PingTelecommand(), 3], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(217, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/pld_1', [i for i in range(0, 4, 1)]), Send, WaitMode.Wait],

    # Wing CAM - low res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(11, '/pld_1_0.jpg', [i for i in range(0, 11, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/pld_1_0.jpg', [i for i in range(11, 22, 1)]), Send, WaitMode.Wait],

    # Nadir CAM - low res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(12, '/pld_1_3.jpg', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],

    # Wing CAM - mid res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(13, '/pld_1_1.jpg', [i for i in range(0, 12, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(14, '/pld_1_1.jpg', [i for i in range(12, 25, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(15, '/pld_1_1.jpg', [i for i in range(25, 37, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(16, '/pld_1_1.jpg', [i for i in range(37, 58, 1)]), Send, WaitMode.Wait],

    # Nadir CAM - mid res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(17, '/pld_1_4.jpg', [i for i in range(0, 11, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(18, '/pld_1_4.jpg', [i for i in range(11, 22, 1)]), Send, WaitMode.Wait],

    # Nadir CAM - high res
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/pld_1_5.jpg', [i for i in range(0, 11, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(21, '/pld_1_5.jpg', [i for i in range(11, 22, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(22, '/pld_1_5.jpg', [i for i in range(22, 37, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(23, '/pld_1_5.jpg', [i for i in range(37, 56, 1)]), Send, WaitMode.Wait],

    # Last leop file chunks
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(174, '/leop', [i for i in range(3, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(175, '/leop', [i for i in range(9, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(176, '/leop', [i for i in range(15, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(177, '/leop', [i for i in range(21, 580, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(178, '/leop', [i for i in range(28, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(179, '/leop', [i for i in range(34, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(180, '/leop', [i for i in range(40, 580, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(181, '/leop', [i for i in range(46, 580, 50)]), Send, WaitMode.Wait],
]
