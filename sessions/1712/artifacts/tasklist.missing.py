tasks = [
[tc.DownloadFile(30, '/radfet_20', [9, 11]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [1, 64, 82, 114, 132]), Send, WaitMode.Wait]
]