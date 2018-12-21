tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 108 and 109
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(150, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(156, 350, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 108 and 109
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(153, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(159, 350, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(151, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(152, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(154, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(155, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(157, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(158, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(160, 350, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(161, 350, 12)]), Send, WaitMode.Wait],

    # Download PLD commissioning data
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/pld_2', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],

    # Download PLD commissioning low and med res photos
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(41, '/pld_2_0.jpg', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(42, '/pld_2_1.jpg', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/pld_2_1.jpg', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pld_2_1.jpg', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pld_2_1.jpg', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(46, '/pld_2_3.jpg', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(47, '/pld_2_4.jpg', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/pld_2_4.jpg', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/pld_2_4.jpg', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/pld_2_4.jpg', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],

    # Download PLD commissioning hi res photos
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(51, '/pld_2_2.jpg', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/pld_2_2.jpg', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/pld_2_2.jpg', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/pld_2_2.jpg', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/pld_2_2.jpg', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/pld_2_2.jpg', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/pld_2_2.jpg', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/pld_2_2.jpg', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(61, '/pld_2_5.jpg', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/pld_2_5.jpg', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/pld_2_5.jpg', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/pld_2_5.jpg', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/pld_2_5.jpg', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/pld_2_5.jpg', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/pld_2_5.jpg', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/pld_2_5.jpg', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]