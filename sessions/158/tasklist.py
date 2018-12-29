tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry during sail exp (T+10 to T+30min)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(111, '/telemetry.current', [i for i in range(764, 820, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.current', [i for i in range(770, 820, 12)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(113, '/telemetry.current', [i for i in range(773, 820, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.current', [i for i in range(783, 820, 12)]), Send, WaitMode.Wait],

    # Sail exp photos download (after sail deployment)
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(45, '/sail.photo_45', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/sail.photo_67', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(55, '/sail.photo_55', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/sail.photo_79', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(51, '/sail.photo_51', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/sail.photo_61', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(73, '/sail.photo_73', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/sail.photo_85', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # Sail exp photos download (before sail deployment)
    [tc.DownloadFile(5, '/sail.photo_5', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(15, '/sail.photo_15', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/sail.photo_25', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/sail.photo_35', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More sail exp photos download (after sail deployment)
    [tc.DownloadFile(47, '/sail.photo_47', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/sail.photo_49', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/sail.photo_53', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/sail.photo_57', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/sail.photo_59', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/sail.photo_63', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/sail.photo_65', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/sail.photo_69', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    # More sail exp photos download (before sail deployment)
    [tc.DownloadFile(11, '/sail.photo_11', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/sail.photo_21', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/sail.photo_31', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/sail.photo_41', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 15], SendLoop, WaitMode.NoWait],
]