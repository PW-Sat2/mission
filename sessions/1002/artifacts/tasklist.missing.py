tasks = [
[tc.DownloadFile(30, '/p5_128_0', [20, 25]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p9_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p9_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p9_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 46, 48, 51, 52, 55]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p9_480_0', [56, 57, 59, 60, 63, 64, 65, 66, 67, 68, 69, 80, 83, 84, 87, 89]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/radfet_12', [0, 3, 4, 5, 8, 11, 13, 14, 15]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/p8_128_0', [24, 25, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/p9_128_0', [25]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/p3_480_0', [6, 9, 15, 16, 17, 18, 21, 22, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/p3_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/p3_480_0', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/p3_480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.current', [1233, 1283, 1333, 1383]), Send, WaitMode.Wait]
]