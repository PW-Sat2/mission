tasks = [
[tc.DownloadFile(30, '/telemetry.current', [4, 10, 16, 22, 29, 36, 42, 48, 54, 60, 66, 72, 79, 86, 92]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [98, 104, 110, 116, 122, 129, 136, 142, 148, 154, 160, 166, 172, 179, 186]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1325, 1469, 1475]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_w_480_0', [143]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p2_n_480_0', [82, 83, 84, 85, 86, 87, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/p2_n_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/p2_n_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/p2_n_480_0', [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/p2_w_480_0', [4, 10, 39, 40, 41, 43, 80, 81, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/p2_w_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/p2_w_480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/p2_w_480_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait]
]