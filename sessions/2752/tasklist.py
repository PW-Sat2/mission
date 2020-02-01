tasks = [
    # Generated on 2020-02-01 10:37:40.184052, contains telemetry from sessions 2751 to 2752.
    # The session starts on 2020-02-01 11:52:44+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(20, '/telemetry.current', [1449, 1499, 1549, 1599, 1649, 1474, 1524, 1574, 1624, 1462, 1512, 1562, 1612, 1662, 1486, 1536, 1586, 1636, 1456, 1506]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [1556, 1606, 1656, 1468, 1518, 1568, 1618, 1668, 1480, 1530, 1580, 1630, 1492, 1542, 1592, 1642]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t02w_240_12', [1]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t02w_240_19', [7, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t02w_240_20', [6]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t02w_240_21', [5, 6, 7]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02w_240_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t02w_240_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t02w_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t02w_240_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t02w_240_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t02w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t03w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t03w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t03w_240_10', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t03w_240_11', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t03w_240_12', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t03w_240_13', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t03w_240_14', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t03w_240_15', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t03w_240_16', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t03w_240_17', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t03w_240_18', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t03w_240_19', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t03w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t03w_240_20', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t03w_240_21', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t03w_240_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t03w_240_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t03w_240_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t03w_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t03w_240_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t03w_240_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t03w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t03w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t03w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t03w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t03w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t03w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t03w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t03w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t04w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t04w_240_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t04w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t04w_240_1', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t04w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t04w_240_2', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t04w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t04w_240_3', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t04w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t04w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t04w_240_6', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t04w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t04w_240_4', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t04w_240_4', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/t04w_240_4', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/t04w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/t04w_240_5', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/t04w_240_5', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/t04w_240_5', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
