tasks = [
[tc.DownloadFile(30, '/telemetry.current', [8, 46, 58, 84, 96, 108, 134, 146, 158, 184, 196]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [208, 234, 246, 258, 284, 296, 308, 334, 346, 358]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1414, 1426, 1438, 1464, 1476, 1488, 1514, 1526, 1538, 1564, 1576, 1588, 1614, 1626, 1638, 1664]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1676, 1688, 1714, 1726, 1738, 1764, 1776, 1788, 1814, 1826, 1838, 1852, 1864, 1876, 1888, 1902]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [1914, 1926, 1938, 1952, 1964, 1976, 1988, 2002, 2014, 2026, 2038, 2052, 2064, 2076, 2088]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.previous', [2102, 2114, 2126, 2138, 2152, 2164, 2176, 2188, 2202, 2214, 2226, 2238, 2252, 2264, 2276]), Send, WaitMode.Wait]
]