tasks = [
[tc.DownloadFile(30, '/telemetry.current', [11, 48, 61, 74, 80, 86, 98, 118, 124, 148, 168, 174]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/radfet_33', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p1_480_0', [57, 58, 59, 63, 76, 78, 79, 85, 90, 94, 133, 134, 135, 136]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_480_0', [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait]
]