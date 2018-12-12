tasks = [
    [[tc.SetBitrate(130, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(131, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 49 and 50
    [tc.DownloadFile(132, '/telemetry.current', [i for i in range(1490, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/telemetry.current', [i for i in range(1495, 1690, 10)]), Send, WaitMode.Wait],

    #SunS Experiment triggering
    [tc.PerformSunSExperiment(134, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_2'), Send, WaitMode.Wait],

    # More low res photos
    # hor_0 downloaded
    [tc.DownloadFile(140, '/hor_1', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/hor_2', [0, 1, 2, 3, 5, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/hor_3', [2, 3, 4, 5, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/hor_4', [4, 6]), Send, WaitMode.Wait],
    # hor_5 downloaded
    # hor_6 downloaded
    [tc.DownloadFile(144, '/hor_7', [2, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/hor_8', [1, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(146, '/hor_9', [0, 6, 7]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(147, '/hor_10', [0, 1]), Send, WaitMode.Wait],
    [tc.DownloadFile(148, '/hor_11', [0, 3, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(149, '/hor_12', [3, 5, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(150, '/hor_13', [1, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/hor_14', [6, 7]), Send, WaitMode.Wait],
    # hor_15 downloaded
    [tc.DownloadFile(152, '/hor_16', [3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/hor_17', [1, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/hor_18', [1, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/hor_19', [1, 2, 3, 4, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(156, '/hor_20', [0, 1]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(157, '/hor_21', [0, 2, 3, 4, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(158, '/hor_22', [0, 1, 4, 6]), Send, WaitMode.Wait],
    [tc.DownloadFile(159, '/hor_23', [0, 1, 2, 5, 6, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(160, '/hor_24', [0, 1, 2, 3, 4, 5, 6, 7]), Send, WaitMode.Wait],
    # hor_25 downloaded
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(161, '/hor_26', [0, 1, 2, 3, 4, 5, 6, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/hor_27', [0, 1, 2, 3, 4, 5, 6, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(163, '/hor_28', [1, 3, 4, 5, 6, 7]), Send, WaitMode.Wait],

    # Much more telemetry between session 49 and 50
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1491, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(1492, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(1493, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(1494, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(1496, 1690, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(1497, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(1498, 1690, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(1499, 1690, 10)]), Send, WaitMode.Wait],

    # Much more telemetry between session 48 and 49
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(400, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(405, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(401, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(402, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(403, 600, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(404, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(406, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [i for i in range(407, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.current', [i for i in range(408, 600, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [i for i in range(409, 600, 10)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(80, '/telemetry.current', [i for i in range(600, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.current', [i for i in range(605, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.current', [i for i in range(601, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.current', [i for i in range(602, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [i for i in range(603, 800, 10)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(85, '/telemetry.current', [i for i in range(604, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/telemetry.current', [i for i in range(606, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/telemetry.current', [i for i in range(607, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/telemetry.current', [i for i in range(608, 800, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [i for i in range(609, 800, 10)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
