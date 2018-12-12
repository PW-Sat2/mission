tasks = [
    [[tc.SetBitrate(230, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(231, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 50 and 51
    [tc.DownloadFile(232, '/telemetry.current', [i for i in range(1650, 1850, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(233, '/telemetry.current', [i for i in range(1662, 1850, 25)]), Send, WaitMode.Wait],

    # Remove photos
    [tc.RemoveFile(100, '/hor_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(101, '/hor_1'), Send, WaitMode.Wait],
    [tc.RemoveFile(102, '/hor_2'), Send, WaitMode.Wait],
    [tc.RemoveFile(103, '/hor_3'), Send, WaitMode.Wait],
    [tc.RemoveFile(104, '/hor_4'), Send, WaitMode.Wait],
    [tc.RemoveFile(105, '/hor_5'), Send, WaitMode.Wait],
    [tc.RemoveFile(106, '/hor_6'), Send, WaitMode.Wait],
    [tc.RemoveFile(107, '/hor_7'), Send, WaitMode.Wait],
    [tc.RemoveFile(108, '/hor_8'), Send, WaitMode.Wait],
    [tc.RemoveFile(109, '/hor_9'), Send, WaitMode.Wait],
    [tc.ListFiles(234, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(200, '/hor_10'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/hor_11'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/hor_12'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/hor_13'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/hor_14'), Send, WaitMode.Wait],
    [tc.RemoveFile(205, '/hor_15'), Send, WaitMode.Wait],
    [tc.RemoveFile(206, '/hor_16'), Send, WaitMode.Wait],
    [tc.RemoveFile(207, '/hor_17'), Send, WaitMode.Wait],
    [tc.RemoveFile(208, '/hor_18'), Send, WaitMode.Wait],
    [tc.RemoveFile(209, '/hor_19'), Send, WaitMode.Wait],
    [tc.ListFiles(235, '/'), Send, WaitMode.Wait],

    [tc.RemoveFile(210, '/hor_20'), Send, WaitMode.Wait],
    [tc.RemoveFile(211, '/hor_21'), Send, WaitMode.Wait],
    [tc.RemoveFile(212, '/hor_22'), Send, WaitMode.Wait],
    [tc.RemoveFile(213, '/hor_23'), Send, WaitMode.Wait],
    [tc.RemoveFile(214, '/hor_24'), Send, WaitMode.Wait],
    [tc.RemoveFile(215, '/hor_25'), Send, WaitMode.Wait],
    [tc.RemoveFile(216, '/hor_26'), Send, WaitMode.Wait],
    [tc.RemoveFile(217, '/hor_27'), Send, WaitMode.Wait],
    [tc.RemoveFile(218, '/hor_28'), Send, WaitMode.Wait],

    [tc.ListFiles(236, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
