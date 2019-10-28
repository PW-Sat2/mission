tasks = [
[tc.DownloadFile(30, '/telemetry.current', [405, 431, 455, 505, 555, 605, 655, 705, 755, 781, 805, 855, 905]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [1243, 1293, 1443, 1493, 1543, 1593, 1643, 1669, 1693, 1743, 1769, 1793]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t02w_240_28', [3, 4, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t02w_240_28', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t02w_240_28', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t02w_240_28', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait]
]