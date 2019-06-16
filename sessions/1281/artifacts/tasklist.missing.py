tasks = [
[tc.DownloadFile(30, '/p7_480_0', [16, 18]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/suns_ps_7', [1, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/suns_ps_7', [35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 76, 77, 78, 93, 94, 95, 96]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/suns_ps_7', [136, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/suns_ps_7', [194, 195, 196, 197, 199, 200, 201, 202, 203, 206, 210, 211, 217, 218, 226, 239]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [105, 155, 205, 255, 305, 355, 405]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/p2_480_0', [45, 46, 60, 61, 66, 70, 71, 72, 73, 74, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait]
]