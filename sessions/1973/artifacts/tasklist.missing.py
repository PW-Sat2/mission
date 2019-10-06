tasks = [
[tc.DownloadFile(30, '/telemetry.current', [432, 444, 532]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/suns_ps_15', [398, 399, 400]), Send, WaitMode.Wait]
]