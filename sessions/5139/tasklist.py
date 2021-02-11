tasks = [
    # Generated on 2021-02-11 11:02:32.691000, contains telemetry from sessions 5138 to 5139.
    # The session starts on 2021-02-11 11:49:38+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(36, '/telemetry.current', [332, 382, 432, 482, 532, 357, 407, 457, 507, 345, 395, 445, 495, 545, 369, 419, 469, 519, 339, 389]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [439, 489, 539, 351, 401, 451, 501, 363, 413, 463, 513, 375, 425, 475, 525]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [8, 46, 58, 84, 96, 108, 134, 146, 158, 184, 196]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [208, 234, 246, 258, 284, 296, 308, 334, 346, 358]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1414, 1426, 1438, 1464, 1476, 1488, 1514, 1526, 1538, 1564, 1576, 1588, 1614, 1626, 1638, 1664]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1676, 1688, 1714, 1726, 1738, 1764, 1776, 1788, 1814, 1826, 1838, 1852, 1864, 1876, 1888, 1902]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1914, 1926, 1938, 1952, 1964, 1976, 1988, 2002, 2014, 2026, 2038, 2052, 2064, 2076, 2088]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2102, 2114, 2126, 2138, 2152, 2164, 2176, 2188, 2202, 2214, 2226, 2238, 2252, 2264, 2276]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(38, '/photo02n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/photo02n_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/photo02n_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/photo02n_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/photo02n_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/photo02w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/photo02w_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/photo02w_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/photo02w_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/photo02w_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/photo01n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/photo01n_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/photo01n_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/photo01n_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/photo01n_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/photo01w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/photo01w_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/photo01w_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/photo01w_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/photo01w_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]