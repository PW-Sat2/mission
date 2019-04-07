tasks = [
[tc.DownloadFile(30, '/suns_ps_3', [163, 173, 177, 180, 181, 184, 185, 186, 188, 189, 190, 191, 192, 193]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/suns_ps_3', [194, 195, 196, 197, 198, 200, 201, 203, 204, 205, 206, 210, 214, 216]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [570, 620]), Send, WaitMode.Wait]
]