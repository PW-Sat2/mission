tasks = [
[tc.DownloadFile(30, '/telemetry.current', [34, 41, 72, 84, 122, 134]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [78, 84, 240, 360, 703, 716, 928, 990, 1134, 1140, 1146, 1178, 1184, 1190, 1196, 1237, 1261, 1402, 1408, 1414]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1420, 1426, 1432, 1438, 1452, 1458, 1464, 1476, 1482, 1488, 1495, 1502, 1508, 1514, 1526, 1532, 1538, 1552, 1564, 1571]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1576, 1578, 1582, 1584, 1588, 1590, 1602, 1608, 1614, 1628, 1634, 1640, 1652, 1658, 1664, 1678, 1684, 1690, 1702]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [1708, 1714, 1728, 1734, 1740, 1752, 1758, 1764, 1778, 1784, 1790, 1802, 1808, 1814, 1828, 1834, 1840, 1846, 1852]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.previous', [1858, 1864, 1878, 1884, 1890, 1902, 1908, 1914, 1921, 1928, 1934, 1940, 1952, 1958, 1964, 1971, 1978, 1984, 1990]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.previous', [2002, 2008, 2014, 2028, 2034, 2040, 2052, 2058, 2064, 2078, 2084, 2090, 2096, 2102, 2108, 2114, 2128, 2134, 2140]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.previous', [2146, 2152, 2158, 2164, 2178, 2184, 2190, 2196, 2202, 2208, 2214, 2228, 2234, 2240, 2246, 2252, 2258, 2264, 2278]), Send, WaitMode.Wait]
]