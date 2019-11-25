tasks = [
[tc.DownloadFile(30, '/telemetry.current', [4, 11, 18, 24, 30, 36, 42, 48, 54, 61, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [74, 80, 961, 1111, 1174, 1224, 1261, 1274, 1287, 1324]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [2141, 2148, 2154, 2160, 2166, 2172, 2178, 2184, 2191, 2198, 2204, 2210]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [2216, 2222, 2228, 2234, 2241, 2248, 2254, 2260, 2266, 2272, 2278]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t04n_240_18', [8, 9, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t04n_240_19', [10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t04n_240_23', [26, 41, 44]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t04n_240_24', [26, 45, 49, 52, 59, 60, 62]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t04n_240_25', [0, 7, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t04n_240_27', [2, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t04n_240_27', [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t04n_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t04n_240_28', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t04n_240_28', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait]
]