tasks = [
[tc.DownloadFile(30, '/telemetry.current', [285]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1342, 1810, 2117]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t10w_480_0', [77]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t15n_480_0', [16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t17w_480_0', [23, 66, 67, 84, 85, 90, 93]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t18n_480_0', [49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t18w_480_0', [20, 35, 38, 43, 44, 45, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t18w_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t21w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t21w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t21w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t21w_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t07w_480_0', [51, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t07w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/t07w_480_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/t14w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/t14w_480_0', [79, 87, 97, 99, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 131, 138]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/t14w_480_0', [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait]
]