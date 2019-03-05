tasks = [
[tc.DownloadFile(30, '/telemetry.current', [14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [964, 1014, 1064, 1114, 1152, 1164, 1214, 1264, 1314, 1364, 1402, 1414, 1452, 1464, 1502, 1514, 1552, 1564, 1602]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1614, 1652, 1664, 1702, 1714, 1752, 1764, 1802, 1814, 1852, 1864, 1902, 1914, 1952, 2002, 2014, 2052, 2102]), Send, WaitMode.Wait]
]