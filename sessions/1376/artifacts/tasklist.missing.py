tasks = [
[tc.DownloadFile(30, '/p10_240_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [366, 894, 990]), Send, WaitMode.Wait]
]