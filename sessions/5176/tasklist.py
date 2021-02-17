tasks = [
    # Generated on 2021-02-17 22:59:54.885000, contains telemetry from sessions 5175 to 5176.
    # The session starts on 2021-02-18 00:09:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(53, '/telemetry.current', [263, 313, 363, 413, 463, 288, 338, 388, 438, 276, 326, 376, 426, 476, 300, 350, 400, 450, 270, 320]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [370, 420, 470, 282, 332, 382, 432, 294, 344, 394, 444, 306, 356, 406, 456]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(31, '/telemetry.previous', [78, 84, 1237, 1261, 1420, 1426, 1432, 1438, 1452, 1458, 1464, 1476, 1482, 1488, 1495, 1502]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1508, 1514, 1526, 1571, 1576, 1582, 1584, 1658, 1664, 1678, 1684, 1690, 1702, 1778, 1858, 1878]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1884, 1890, 1902, 1908, 1914, 1921, 1928, 2002, 2008, 2014, 2028, 2034, 2040, 2052, 2058, 2064]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p5174_0_n_p480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p5174_0_n_p480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p5174_0_n_p480_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p5174_0_n_p480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p5174_1_w_p480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p5174_1_w_p480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p5174_1_w_p480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p5174_1_w_p480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p5174_1_w_p480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p5174_1_w_p480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p5174_1_w_p480_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p5174_1_w_p480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p5174_1_w_p480_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p5174_1_w_p480_0', [164, 165, 166]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]