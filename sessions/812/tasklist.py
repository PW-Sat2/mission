tasks = [
    # Generated on 2019-04-06 23:01:23.507363, contains telemetry from sessions 811 to 812.
    # The session starts on 2019-04-06 23:57:19+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(36, '/telemetry.current', [1378, 1428, 1478, 1528, 1578, 1403, 1453, 1503, 1553, 1603, 1391, 1441, 1491, 1541, 1591, 1415, 1465, 1515, 1565, 1385]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1435, 1485, 1535, 1585, 1397, 1447, 1497, 1547, 1597, 1409, 1459, 1509, 1559, 1421, 1471, 1521, 1571]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p7_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p7_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p7_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p7_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p8_480_0', [100, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 117, 118, 119, 120, 121]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p8_480_0', [122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(38, 'p1_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(39, 'p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(40, 'radfet_10'), Send, WaitMode.Wait],
    [tc.ListFiles(41, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]