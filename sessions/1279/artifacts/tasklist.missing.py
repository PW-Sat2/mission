tasks = [
[tc.DownloadFile(30, '/p7_480_0', [16, 18]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p2_480_0', [37, 45, 46, 60, 61, 66, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p2_480_0', [74, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p3_480_0', [25]), Send, WaitMode.Wait]
]