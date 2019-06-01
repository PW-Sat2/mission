tasks = [
[tc.DownloadFile(30, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p7_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p3_128_0', [21]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_480_0', [0, 2, 4, 6, 15, 16, 17, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p1_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/p4_128_0', [7]), Send, WaitMode.Wait]
]