tasks = [
[tc.DownloadFile(30, '/telemetry.current', [570, 620, 750, 788, 800, 812, 838, 862, 888, 912, 950, 962, 1000, 1012]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [1038, 1050, 1062, 1088, 1112, 1150, 1162, 1200, 1212, 1226, 1238, 1262, 1288, 1312]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1338, 1362, 1388, 1400, 1412, 1438, 1450, 1462, 1488, 1500, 1512, 1538, 1562, 1612]), Send, WaitMode.Wait]
]