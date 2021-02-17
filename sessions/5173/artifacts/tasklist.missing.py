tasks = [
[tc.DownloadFile(30, '/telemetry.current', [78, 84, 240, 360, 703, 716, 928, 990, 1134, 1140, 1146, 1178, 1184, 1190, 1196]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [1237, 1261, 1402, 1408, 1414, 1420, 1426, 1432, 1438, 1452, 1458, 1464, 1476, 1482]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1488, 1495, 1502, 1508, 1514, 1526, 1532, 1538, 1552, 1564, 1576, 1582, 1588, 1602]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_w_p480_0', [22, 53, 54, 58, 59]), Send, WaitMode.Wait]
]