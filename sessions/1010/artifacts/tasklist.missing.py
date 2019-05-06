tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1760, 1872, 2160, 2210, 2222, 2272]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [292]), Send, WaitMode.Wait]
]