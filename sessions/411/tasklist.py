tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1385, 1435, 1485, 1535, 1585, 1410, 1460, 1510, 1560, 1398, 1448, 1498, 1548, 1598, 1422, 1472, 1522, 1572, 1392, 1442]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1492, 1542, 1592, 1404, 1454, 1504, 1554, 1604, 1416, 1466, 1516, 1566, 1428, 1478, 1528, 1578]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(40, '/telemetry.previous', [1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1507, 1519, 1557, 1569, 1607]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.previous', [1619, 1657, 1669, 1707, 1719, 1757, 1769, 1807, 1819, 1857, 1869, 1907, 1919, 1957]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.previous', [1969, 2007, 2019, 2057, 2069, 2107, 2119, 2157, 2169, 2207, 2219, 2257, 2269]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [39, 89, 139, 189, 239, 289, 339, 389, 427, 439, 477, 489, 527, 539, 577, 589]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.current', [627, 639, 677, 689, 727, 739, 777, 789, 827, 839, 877, 889, 927, 939, 977, 989]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.current', [1027, 1039, 1077, 1089, 1127, 1139, 1177, 1189, 1227, 1239, 1277, 1289, 1327, 1339, 1377, 1389]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]