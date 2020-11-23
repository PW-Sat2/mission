tasks = [
[tc.DownloadFile(30, '/telemetry.current', [478, 528, 545]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1946, 2034, 2084, 2122]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/n_w_7_0', [33, 35, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/n_w_7_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/n_w_8_0', [19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/n_w_8_0', [66, 67, 70, 106, 117, 118, 126, 127, 132, 133, 137, 143, 144, 145, 146]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/n_w_8_0', [147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait]
]