tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [3, 15, 53, 115, 165, 203, 215, 253, 265, 315, 365, 415, 465, 503, 515, 565, 615, 665, 703]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [715, 753, 765, 815, 865, 903, 915, 965, 1015, 1065, 1115, 1165, 1215, 1253, 1265, 1315, 1365, 1403, 1415]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [1465, 1503, 1515, 1565, 1603, 1615, 1653, 1665, 1715, 1765, 1815, 1865, 1903, 1915, 1941, 1953, 1965, 2003, 2015]), Send, WaitMode.Wait]
]