tasks = [
[tc.DownloadFile(30, '/t02w_240_17', [18]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t01w_240_11', [35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t01w_240_12', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t01w_240_12', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t01w_240_13', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t01w_240_13', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t01w_240_14', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t01w_240_14', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t01w_240_20', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t01w_240_20', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t01w_240_21', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t01w_240_21', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t01w_240_22', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t01w_240_22', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/t01w_240_3', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/t01w_240_3', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/t01w_240_7', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/t01w_240_7', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/t02w_240_14', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/t02w_240_14', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/t02w_240_15', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/t02w_240_15', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/t02w_240_2', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/t02w_240_2', [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/t02w_240_22', [7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/t02w_240_22', [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/t02w_240_23', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/t02w_240_23', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
	[tc.DownloadFile(58, '/t02w_240_24', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(59, '/t02w_240_24', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(60, '/t02w_240_25', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(61, '/t02w_240_25', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(62, '/t02w_240_27', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
	[tc.DownloadFile(63, '/t02w_240_27', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(64, '/t02w_240_3', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(65, '/t02w_240_3', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
	[tc.DownloadFile(66, '/t02w_240_4', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(67, '/t02w_240_4', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(68, '/t02w_240_8', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(69, '/t02w_240_8', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(70, '/t01w_240_15', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(71, '/t01w_240_15', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(72, '/t01w_240_15', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(73, '/t01w_240_16', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(74, '/t01w_240_16', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(75, '/t01w_240_16', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(76, '/t01w_240_17', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(77, '/t01w_240_17', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(78, '/t01w_240_17', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(79, '/t01w_240_18', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(80, '/t01w_240_18', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(81, '/t01w_240_18', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(82, '/t01w_240_19', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(83, '/t01w_240_19', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(84, '/t01w_240_19', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(85, '/t01w_240_4', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(86, '/t01w_240_4', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(87, '/t01w_240_4', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
	[tc.DownloadFile(88, '/t02w_240_10', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(89, '/t02w_240_10', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(90, '/t02w_240_10', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(91, '/t02w_240_11', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(92, '/t02w_240_11', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(93, '/t02w_240_11', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
	[tc.DownloadFile(94, '/t02w_240_12', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(95, '/t02w_240_12', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(96, '/t02w_240_12', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
	[tc.DownloadFile(97, '/t02w_240_13', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(98, '/t02w_240_13', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(99, '/t02w_240_13', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
	[tc.DownloadFile(100, '/t02w_240_26', [8, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(101, '/t02w_240_26', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(102, '/t02w_240_26', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(103, '/t02w_240_28', [7, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(104, '/t02w_240_28', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(105, '/t02w_240_28', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(106, '/t02w_240_5', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(107, '/t02w_240_5', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(108, '/t02w_240_5', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
	[tc.DownloadFile(109, '/t02w_240_6', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(110, '/t02w_240_6', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(111, '/t02w_240_6', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(112, '/t02w_240_7', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(113, '/t02w_240_7', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(114, '/t02w_240_7', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(115, '/t02w_240_9', [3, 10, 14, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(116, '/t02w_240_9', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
	[tc.DownloadFile(117, '/t02w_240_9', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait]
]