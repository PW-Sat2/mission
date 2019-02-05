tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1507, 1519, 1557, 1569, 1607]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1619, 1657, 1669, 1707, 1719, 1757, 1769, 1807, 1819, 1857, 1869, 1907, 1919, 1957]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1969, 2007, 2019, 2057, 2069, 2107, 2119, 2157, 2169, 2207, 2219, 2257, 2269]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [39, 89, 139, 189, 239, 277, 289, 339, 389, 427, 439, 477, 489, 527, 539, 577, 589]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [627, 639, 677, 689, 727, 739, 777, 789, 827, 839, 877, 889, 927, 939, 977, 989]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [1027, 1039, 1077, 1089, 1127, 1139, 1177, 1189, 1227, 1239, 1277, 1289, 1327, 1339, 1377, 1389]), Send, WaitMode.Wait]
]