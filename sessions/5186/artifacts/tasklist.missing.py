tasks = [
[tc.DownloadFile(30, '/p1_n_480_0', [0, 19, 25, 27, 29, 30, 31, 32, 33, 34, 39, 41, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p2_w_480_0', [0, 1, 2, 4, 10, 39, 40, 41, 43, 80, 81]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p1_n_480_0', [57, 59, 60, 64, 65, 80, 81, 93, 94, 95, 96, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_w_480_0', [60, 61, 63, 64, 80, 81, 95]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p2_n_480_0', [82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait]
]