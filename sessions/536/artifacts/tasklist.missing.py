tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1473, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1823]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1835, 1885, 1923, 1935, 1973, 1985, 2023, 2035, 2073, 2085, 2123, 2135, 2173, 2185, 2223, 2235, 2273]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 543, 555, 605, 655, 705, 755, 793]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [805, 843, 855, 893, 905, 943, 955, 993, 1005, 1043, 1055, 1093, 1105, 1143, 1155, 1193, 1205]), Send, WaitMode.Wait]
]