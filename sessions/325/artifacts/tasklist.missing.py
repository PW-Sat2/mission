tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1133, 1183, 1233, 1333, 1433, 1633, 1783, 1971, 1983, 2033, 2133, 2221, 2271]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [3, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 553, 591, 603]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [641, 653, 691, 703, 741, 841, 853, 891, 903, 941, 953, 1003, 1041, 1053]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [1091, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653]), Send, WaitMode.Wait]
]