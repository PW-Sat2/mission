tasks = [
    # Generated on 2020-07-12 21:39:51.390000, contains telemetry from sessions 3804 to 3805.
    # The session starts on 2020-07-12 22:56:28+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(55, '/telemetry.current', [1355, 1405, 1455, 1505, 1555, 1380, 1430, 1480, 1530, 1368, 1418, 1468, 1518, 1568, 1392, 1442, 1492, 1542, 1362, 1412]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [1462, 1512, 1562, 1374, 1424, 1474, 1524, 1386, 1436, 1486, 1536, 1398, 1448, 1498, 1548]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [528, 540, 565, 578, 628, 640, 652, 678, 690, 702, 715, 740, 752, 790, 815, 828, 852, 872, 878]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [902, 928, 940, 952, 965, 1015, 1040, 1052, 1072, 1090, 1096, 1115, 1165, 1178, 1190, 1240, 1265, 1290, 1352]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_w_13_02_0', [21, 108, 109, 110, 135, 141, 143, 144, 146, 147, 148, 149, 150, 152, 153, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_w_13_46_0', [38, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_13_46_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_13_46_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_13_46_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_13_46_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_13_46_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_13_47_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_13_47_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_13_47_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_13_47_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_w_13_47_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_13_47_0', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_w_13_47_0', [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_13_47_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_13_48_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_13_48_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_13_48_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_13_48_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_13_48_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_13_48_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_w_13_48_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_13_48_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]