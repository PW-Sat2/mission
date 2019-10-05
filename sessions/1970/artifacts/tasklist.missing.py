tasks = [
[tc.DownloadFile(30, '/telemetry.current', [1257, 1269, 1357]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t01n_480_0', [9]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t01w_480_0', [20, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t02n_480_0', [19, 22, 24, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t02w_480_0', [35, 36]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t03n_480_0', [24, 28]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t03w_480_0', [18, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t04n_480_0', [7, 8, 11, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t04w_480_0', [3, 29]), Send, WaitMode.Wait]
]