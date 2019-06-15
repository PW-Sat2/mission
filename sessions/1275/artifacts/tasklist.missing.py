tasks = [
[tc.DownloadFile(30, '/p10_128_0', [18]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p9_128_0', [10, 11, 12]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p1_480_0', [11, 30, 31, 32, 33, 37, 39, 51, 64, 65, 99, 100, 101, 110, 111, 120, 121]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_480_0', [122, 123, 125, 126, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p1_480_0', [142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]), Send, WaitMode.Wait]
]