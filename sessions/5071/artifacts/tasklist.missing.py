tasks = [
[tc.DownloadFile(30, '/telemetry.current', [14, 314]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [294, 644, 2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait]
]