tasks = [
    # Generated on 2019-10-27 12:40:57.709000, contains telemetry from sessions 2115 to 2116.
    # The session starts on 2019-10-27 13:01:41+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(83, '/telemetry.current', [1623, 1673, 1723, 1773, 1823, 1648, 1698, 1748, 1798, 1636, 1686, 1736, 1786, 1836, 1660, 1710, 1760, 1810, 1630, 1680]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/telemetry.current', [1730, 1780, 1830, 1642, 1692, 1742, 1792, 1842, 1654, 1704, 1754, 1804, 1666, 1716, 1766, 1816, 582, 882]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/t02w_240_0', [1, 3]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t02w_240_1', [1]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02w_240_11', [20]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t02w_240_13', [38, 40, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t02w_240_15', [23, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t02w_240_18', [52, 53, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t02w_240_19', [15, 31, 33, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t02w_240_2', [0, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t02w_240_20', [9, 10, 14, 15, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t02w_240_23', [5, 7, 30]), Send, WaitMode.Wait],

    [tc.DownloadFile(33, '/t02w_240_10', [1, 3, 4, 6, 7, 10, 11, 12, 15, 16, 42, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t02w_240_14', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t02w_240_24', [0, 32, 33, 34, 35, 43, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t02w_240_21', [0, 16, 17, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t02w_240_21', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t02w_240_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t02w_240_22', [10, 11, 12, 13, 14, 15, 16, 23, 24, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t02w_240_25', [14, 16, 20, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t02w_240_25', [44, 45, 46, 47, 48, 49, 50, 51, 52, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t02w_240_26', [5, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t02w_240_26', [38, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t02w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t02w_240_3', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t02w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t02w_240_4', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t02w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t02w_240_5', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t02w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t02w_240_6', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t02w_240_16', [5, 8, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t02w_240_16', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02w_240_16', [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t02w_240_17', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t02w_240_17', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t02w_240_17', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t02w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t02w_240_7', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t02w_240_7', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t02w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t02w_240_8', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t02w_240_8', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t02w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t02w_240_9', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t02w_240_9', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t02w_240_27', [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/t02w_240_27', [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/t02w_240_27', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/t02w_240_27', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/t02w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/t02w_240_28', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/t02w_240_28', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/t02w_240_28', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]