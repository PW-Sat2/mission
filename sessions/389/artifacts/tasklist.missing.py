tasks = [
[tc.DownloadFile(30, '/p7_128_0', [12]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p9_128_0', [4, 7, 8, 9, 11, 12]), Send, WaitMode.Wait]
]