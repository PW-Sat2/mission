tasks = [
    # Generated on 2019-12-23 18:35:49.733000, contains telemetry from sessions 2490 to 2492.
    # The session starts on 2019-12-23 19:28:41+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(20, '/telemetry.current', [865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 890, 940]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 878, 928, 978, 1028]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 902, 952, 1002, 1052, 1102, 1152]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 872, 922, 972, 1022, 1072, 1122, 1172, 1222]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [1496, 1546, 1596, 1646, 1696, 1746, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [1608, 1658, 1708]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(29, '/t03w_240_9', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait], 
    [tc.DownloadFile(30, '/t03w_240_19', [48, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t03w_240_22', [16, 21, 22, 23, 24, 25, 27, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t03w_240_23', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t03w_240_23', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t03w_240_24', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t03w_240_24', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t03w_240_25', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t03w_240_25', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t03w_240_26', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t03w_240_26', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t03w_240_26', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t03w_240_27', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t03w_240_27', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t03w_240_27', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t03w_240_28', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t03w_240_28', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t03w_240_28', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],

    [tc.DownloadFile(48, '/t04w_240_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t04w_240_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t04w_240_1', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t04w_240_1', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t04w_240_2', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t04w_240_2', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t04w_240_3', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t04w_240_4', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t04w_240_5', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t04w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
     
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]