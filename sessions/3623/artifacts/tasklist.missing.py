tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1662, 1812]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p10_0', [23, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p8_0', [69, 70]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p9_0', [32, 35, 38, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t3w_0', [46, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t4n_0', [21, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t4w_0', [17, 51, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t5n_0', [20, 67, 131, 132, 152, 153]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t5w_0', [37, 68, 70, 74, 100, 101]), Send, WaitMode.Wait]
]