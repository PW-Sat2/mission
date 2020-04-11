tasks = [
[tc.DownloadFile(30, '/telemetry.current', [162]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p5_128_0', [16, 17]), Send, WaitMode.Wait]
]