tasks = [
[tc.DownloadFile(30, '/telemetry.current', [4, 54, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p10_128_0', [12, 13, 14]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p7_128_0', [16]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p9_128_0', [4, 14, 15]), Send, WaitMode.Wait]
]