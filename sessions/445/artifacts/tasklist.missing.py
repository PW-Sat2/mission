tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2184, 2196, 2246]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 642, 666, 716, 766, 816, 866, 916]), Send, WaitMode.Wait]
]