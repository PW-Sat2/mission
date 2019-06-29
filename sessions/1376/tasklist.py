tasks = [
    # Generated on 2019-06-28 23:21:15.499000, contains telemetry from sessions 1372 to 1373.
    # The session starts on 2019-06-29 12:53:16+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # man-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(180, 1760, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(204, 1760, 48)]), Send, WaitMode.Wait],

    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(192, 1760, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(216, 1760, 48)]), Send, WaitMode.Wait],
    # man-generated telemetry end

    # Download 16th RadFET data
    [tc.DownloadFile(60, '/radfet_16', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/radfet_16', range(8, 16)), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # file download start
    [tc.DownloadFile(100, '/p1_240_0', [i for i in range(70, 76, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(101, '/p3_240_0', [0, 7, 8, 137, 138, 11, 13, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_240_0', [18, 23, 26, 27, 28, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p3_240_0', [77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p4_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p4_240_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p4_240_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p4_240_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],

    [tc.DownloadFile(120, '/p5_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/p5_240_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],

    [tc.DownloadFile(130, '/p6_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],

    [tc.DownloadFile(140, '/p7_240_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/p7_240_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/p7_240_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/p7_240_0', [72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # man-generated telemetry start
    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(186, 1760, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(198, 1760, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(210, 1760, 48)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(222, 1760, 48)]), Send, WaitMode.Wait],
    # man-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(190, '/p2_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(191, '/p2_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(192, '/p2_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(193, '/p2_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(194, '/p2_480_0', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(195, '/p2_480_0', [i for i in range(100, 111, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Bonus --------

    [tc.DownloadFile(150, '/p8_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/p8_240_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/p8_240_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/p8_240_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/p8_240_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],

    [tc.DownloadFile(160, '/p9_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/p9_240_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/p9_240_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(163, '/p9_240_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(164, '/p9_240_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],

    [tc.DownloadFile(170, '/p10_128_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/p10_128_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(180, '/p10_240_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(181, '/p10_240_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(182, '/p10_240_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(183, '/p10_240_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(184, '/p10_240_0', [i for i in range(80, 90, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]