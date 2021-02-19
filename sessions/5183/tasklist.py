tasks = [
    # Generated on 2021-02-19 00:57:11.432557, contains telemetry from sessions 5182 to 5183.
    # The session starts on 2021-02-19 11:39:24+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1825, 1875, 1925, 1975, 2025, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1338, 1388, 1438, 1488, 1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 862, 912, 962, 1012, 1062]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1832, 1882, 1932, 1982, 2032, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 868, 918, 968, 1018, 1068]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1118, 1168, 1218, 1268, 1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(40, '/n01n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/n01n_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/n01n_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/n01n_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/n01n_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/n01n_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/n01w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/n01w_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/n01w_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/n01w_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/n01w_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/n01w_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/n01w_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/n01w_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/n02n_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/n02n_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/n02n_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/n02n_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/n02n_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/n02n_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/n02n_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/n02n_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/n02n_0', [151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/n02w_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/n02w_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/n02w_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/n02w_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/n02w_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
