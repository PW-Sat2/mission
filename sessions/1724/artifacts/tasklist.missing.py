tasks = [
[tc.DownloadFile(30, '/t17w_128_0', [24]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t12w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t12w_480_0', [42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t12w_480_0', [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 136]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t12w_128_0', [1, 26]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t13w_128_0', [32]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t14w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t14w_128_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t14n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t13n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t13n_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t12n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t16w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t16w_128_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait]
]