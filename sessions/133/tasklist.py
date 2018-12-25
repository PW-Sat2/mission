tasks = [
    # ============================================================================
    # SESSION 133
    # ============================================================================

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    ["List files - 13 items expected", Print, WaitMode.Wait],

    ["Telemetry current between sessions  131 and 132", Print, WaitMode.Wait],

    # Telemetry between session 131 and 132
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(101, '/telemetry.current', [i for i in range(300, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [i for i in range(325, 1600, 60)]), Send, WaitMode.Wait],

    [tc.DownloadFile(103, '/telemetry.current', [i for i in range(312, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.current', [i for i in range(337, 1600, 60)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(105, '/telemetry.current', [i for i in range(306, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [i for i in range(318, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [i for i in range(331, 1600, 60)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [i for i in range(343, 1600, 60)]), Send, WaitMode.Wait],

    # Telemetry between session 130 and 131
    ["Telemetry current between sessions  130 and 131", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(130, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(136, 300, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(12, '/telemetry.current', [i for i in range(133, 300, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(13, '/telemetry.current', [i for i in range(139, 300, 12)]), Send, WaitMode.Wait],

    # Remove SunS files
    ["Remove SunS files", Print, WaitMode.Wait],

    [tc.RemoveFile(20, '/suns_8'), Send, WaitMode.NoWait],
    [tc.RemoveFile(21, '/suns_8_sec'), Send, WaitMode.NoWait],

    [tc.ListFiles(22, '/'), Send, WaitMode.Wait],

    # RadFET exp data download
    ["RadFET experiment data download", Print, WaitMode.Wait],

    [tc.DownloadFile(30, '/radfet_7', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/radfet_7', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    # High res photos download
    ["Hi-res photos download", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(32, '/p6_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p6_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p6_480_0', [i for i in range(40, 62, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(35, '/p5_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p5_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p5_480_0', [i for i in range(40, 62, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(38, '/p8_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p8_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p8_480_0', [i for i in range(40, 51, 1)]), Send, WaitMode.Wait],

    # Much more telemetry between session 128 and 130
    ["Much more telemetry between session 128 and 130", Print, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1401, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1402, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1404, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [i for i in range(1405, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(1407, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(1408, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(1410, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [i for i in range(1411, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(58, '/telemetry.previous', [i for i in range(1413, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [i for i in range(1414, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.previous', [i for i in range(1416, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [i for i in range(1417, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(62, '/telemetry.previous', [i for i in range(1419, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [i for i in range(1420, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.previous', [i for i in range(1422, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.previous', [i for i in range(1423, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(66, '/telemetry.previous', [i for i in range(1424, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.previous', [i for i in range(1426, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.previous', [i for i in range(1427, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.previous', [i for i in range(1429, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(70, '/telemetry.previous', [i for i in range(1430, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.previous', [i for i in range(1432, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.previous', [i for i in range(1433, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.previous', [i for i in range(1436, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(74, '/telemetry.previous', [i for i in range(1438, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.previous', [i for i in range(1439, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.previous', [i for i in range(1440, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.previous', [i for i in range(1441, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(78, '/telemetry.previous', [i for i in range(1442, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.previous', [i for i in range(1444, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.previous', [i for i in range(1446, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.previous', [i for i in range(1447, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/telemetry.previous', [i for i in range(1448, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/telemetry.previous', [i for i in range(1449, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]