tasks = [
[tc.DownloadFile(30, '/p2_128_0', [0, 1, 3, 5, 8, 10, 14, 16, 17, 19, 20, 22, 26, 27, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p5_128_0', [5]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 18, 20, 23, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [25]), Send, WaitMode.Wait]
]