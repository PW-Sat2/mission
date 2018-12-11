tasks = [
    [[tc.SetBitrate(30, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(31, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 48 and 49
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(400, 1400, 100)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(450, 1400, 100)]), Send, WaitMode.Wait],

    # Goodbye satellite with 9600
    [tc.SetBitrate(34, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # More telemetry download between session 48 and 49
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(400, 1480, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [i for i in range(408, 1480, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [i for i in range(416, 1480, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [i for i in range(432, 1480, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [i for i in range(440, 1480, 50)]), Send, WaitMode.Wait],

    # Some low res photo downloading
    [tc.DownloadFile(40, '/hor_0', [1]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/hor_10', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/hor_20', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/hor_25', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],

    # More low res photos
    [tc.DownloadFile(44, '/hor_1', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/hor_2', [i for i in range(0, 9, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/hor_3', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/hor_4', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    # hor_5 downloaded
    [tc.DownloadFile(48, '/hor_6', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/hor_7', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/hor_8', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/hor_9', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(52, '/hor_11', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/hor_12', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/hor_13', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/hor_14', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    # hor_15 downloaded
    [tc.DownloadFile(56, '/hor_16', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/hor_17', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/hor_18', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/hor_19', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(60, '/hor_21', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/hor_22', [i for i in range(0, 9, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/hor_23', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/hor_24', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(64, '/hor_26', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/hor_27', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/hor_28', [i for i in range(0, 8, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
