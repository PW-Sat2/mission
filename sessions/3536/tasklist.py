tasks = [
    # Generated on 2020-05-31 21:44:19.983000, contains telemetry from sessions 3535 to 3536.
    # The session starts on 2020-05-31 22:46:45+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(78, '/telemetry.current', [1537, 1587, 1637, 1687, 1737, 1562, 1612, 1662, 1712, 1550, 1600, 1650, 1700, 1750, 1574, 1624, 1674, 1724, 1544, 1594]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.current', [1644, 1694, 1744, 1556, 1606, 1656, 1706, 1568, 1618, 1668, 1718, 1580, 1630, 1680, 1730]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [700, 712, 724, 730, 736, 750, 762, 774, 780, 786, 800, 812, 824, 830, 836, 850, 862]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [874, 880, 886, 900, 906, 912, 924, 930, 936, 950, 956, 962, 974, 980, 986, 1000, 1006]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1012, 1024, 1030, 1036, 1050, 1056, 1062, 1074, 1080, 1086, 1100, 1106, 1112, 1124, 1130, 1136, 1150]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1156, 1162, 1174, 1180, 1186, 1200, 1206, 1212, 1224, 1230, 1236, 1250, 1256, 1262, 1274, 1280, 1286]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1300, 1306, 1312, 1324, 1330, 1336, 1350, 1356, 1362, 1374, 1380, 1386, 1400, 1406, 1412, 1424, 1430]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1436, 1450, 1456, 1462, 1474, 1480, 1486, 1500, 1506, 1512, 1524, 1530, 1536, 1550, 1556, 1562, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a5w_480_12_20_0', [57, 59, 60, 61, 64, 66, 67, 68, 69, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a5w_480_12_20_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a6n_480_12_21_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a6n_480_12_21_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a6n_480_12_21_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a6w_480_12_21_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a6w_480_12_21_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a6w_480_12_21_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a6w_480_12_21_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a6w_480_12_21_0', [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a6w_480_12_21_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a6w_480_12_21_0', [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a7n_480_12_22_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a7n_480_12_22_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a7n_480_12_22_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a7n_480_12_22_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a7w_480_12_22_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a7w_480_12_22_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a7w_480_12_22_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a7w_480_12_22_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a7w_480_12_22_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a8n_480_12_23_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a8n_480_12_23_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a8n_480_12_23_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a8n_480_12_23_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a8w_480_12_23_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a8w_480_12_23_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a8w_480_12_23_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a8w_480_12_23_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a8w_480_12_23_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a9n_480_12_24_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a9n_480_12_24_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a9n_480_12_24_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a9n_480_12_24_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/a9w_480_12_24_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a9w_480_12_24_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a9w_480_12_24_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/a9w_480_12_24_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/a9w_480_12_24_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a9w_480_12_24_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/a9w_480_12_24_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/a9w_480_12_24_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]