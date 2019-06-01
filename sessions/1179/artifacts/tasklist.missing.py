tasks = [
[tc.DownloadFile(30, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p7_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p3_128_0', [21]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p4_128_0', [7]), Send, WaitMode.Wait]
]