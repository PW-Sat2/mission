tasks = [
[tc.DownloadFile(30, '/telemetry.current', [155, 168]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t1n_480_0', [30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t1n_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t1n_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t1n_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t1w_480_0', [20, 21, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t1w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t1w_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t1w_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t2n_480_0', [20, 21, 22, 24, 26, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t2n_480_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t2n_480_0', [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t2n_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t3n_480_0', [1, 27, 28, 29, 30, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/t3n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/t3n_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/t3n_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/t3w_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/t3w_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/t3w_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/t3w_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/t4n_480_0', [20, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/t4n_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/t4n_480_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/t4n_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/t4w_480_0', [20, 32, 34, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/t4w_480_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/t4w_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(58, '/t4w_480_0', [85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(59, '/t2w_480_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(60, '/t2w_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(61, '/t2w_480_0', [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(62, '/t2w_480_0', [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
	[tc.DownloadFile(63, '/t2w_480_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(64, '/t5n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(65, '/t5n_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(66, '/t5n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(67, '/t5n_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(68, '/t5n_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(69, '/t5w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(70, '/t5w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(71, '/t5w_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(72, '/t5w_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(73, '/t5w_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(74, '/t6n_480_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(75, '/t6n_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(76, '/t6n_480_0', [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(77, '/t6n_480_0', [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
	[tc.DownloadFile(78, '/t6n_480_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(79, '/t6w_480_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(80, '/t6w_480_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(81, '/t6w_480_0', [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(82, '/t6w_480_0', [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
	[tc.DownloadFile(83, '/t6w_480_0', [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait]
]