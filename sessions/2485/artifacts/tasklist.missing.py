tasks = [
[tc.DownloadFile(30, '/t01w_240_26', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t01w_240_26', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t01w_240_26', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/t01w_240_27', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/t01w_240_27', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/t01w_240_27', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/t01w_240_28', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/t01w_240_28', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/t01w_240_28', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/t01w_240_28', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/t02w_240_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/t02w_240_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/t02w_240_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/t02w_240_1', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/t02w_240_1', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/t02w_240_10', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/t02w_240_10', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/t02w_240_10', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/t02w_240_11', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/t02w_240_11', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/t02w_240_11', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/t02w_240_11', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/t02w_240_12', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/t02w_240_12', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/t02w_240_12', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/t02w_240_12', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/t02w_240_13', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/t02w_240_13', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(58, '/t02w_240_13', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(59, '/t02w_240_14', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(60, '/t02w_240_14', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(61, '/t02w_240_14', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(62, '/t02w_240_15', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(63, '/t02w_240_15', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(64, '/t02w_240_15', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(65, '/t02w_240_16', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(66, '/t02w_240_16', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(67, '/t02w_240_16', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
	[tc.DownloadFile(68, '/t02w_240_17', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(69, '/t02w_240_17', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(70, '/t02w_240_17', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
	[tc.DownloadFile(71, '/t02w_240_18', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
	[tc.DownloadFile(72, '/t02w_240_18', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(73, '/t02w_240_18', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
	[tc.DownloadFile(74, '/t02w_240_19', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(75, '/t02w_240_19', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(76, '/t02w_240_2', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(77, '/t02w_240_2', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(78, '/t02w_240_20', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(79, '/t02w_240_20', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(80, '/t02w_240_21', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(81, '/t02w_240_21', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]), Send, WaitMode.Wait],
	[tc.DownloadFile(82, '/t02w_240_22', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(83, '/t02w_240_22', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
	[tc.DownloadFile(84, '/t02w_240_23', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(85, '/t02w_240_23', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(86, '/t02w_240_24', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(87, '/t02w_240_24', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(88, '/t02w_240_25', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(89, '/t02w_240_25', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(90, '/t02w_240_26', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(91, '/t02w_240_26', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
	[tc.DownloadFile(92, '/t02w_240_27', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(93, '/t02w_240_27', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(94, '/t02w_240_28', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(95, '/t02w_240_28', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(96, '/t02w_240_3', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(97, '/t02w_240_3', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(98, '/t02w_240_4', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(99, '/t02w_240_4', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(100, '/t02w_240_5', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(101, '/t02w_240_5', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
	[tc.DownloadFile(102, '/t02w_240_6', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(103, '/t02w_240_6', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
	[tc.DownloadFile(104, '/t02w_240_7', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(105, '/t02w_240_7', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(106, '/t02w_240_7', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
	[tc.DownloadFile(107, '/t02w_240_8', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(108, '/t02w_240_8', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(109, '/t02w_240_8', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
	[tc.DownloadFile(110, '/t02w_240_9', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(111, '/t02w_240_9', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(112, '/t02w_240_9', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
	[tc.DownloadFile(113, '/t03w_240_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(114, '/t03w_240_1', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
	[tc.DownloadFile(115, '/t03w_240_10', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(116, '/t03w_240_11', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(117, '/t03w_240_12', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(118, '/t03w_240_13', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
	[tc.DownloadFile(119, '/t03w_240_14', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(120, '/t03w_240_15', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(121, '/t03w_240_16', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
	[tc.DownloadFile(122, '/t03w_240_17', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(123, '/t03w_240_18', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
	[tc.DownloadFile(124, '/t03w_240_18', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
	[tc.DownloadFile(125, '/t03w_240_19', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(126, '/t03w_240_19', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(127, '/t03w_240_19', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(128, '/t03w_240_2', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(129, '/t03w_240_2', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(130, '/t03w_240_2', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(131, '/t03w_240_20', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(132, '/t03w_240_20', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
	[tc.DownloadFile(133, '/t03w_240_20', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
	[tc.DownloadFile(134, '/t03w_240_21', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(135, '/t03w_240_21', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
	[tc.DownloadFile(136, '/t03w_240_21', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
	[tc.DownloadFile(137, '/t03w_240_21', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
	[tc.DownloadFile(138, '/t03w_240_22', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(139, '/t03w_240_22', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(140, '/t03w_240_22', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
	[tc.DownloadFile(141, '/t03w_240_23', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
	[tc.DownloadFile(142, '/t03w_240_23', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(143, '/t03w_240_24', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
	[tc.DownloadFile(144, '/t03w_240_24', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(145, '/t03w_240_25', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(146, '/t03w_240_25', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(147, '/t03w_240_26', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(148, '/t03w_240_26', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(149, '/t03w_240_26', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(150, '/t03w_240_27', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(151, '/t03w_240_27', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(152, '/t03w_240_27', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
	[tc.DownloadFile(153, '/t03w_240_28', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(154, '/t03w_240_28', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(155, '/t03w_240_28', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(156, '/t03w_240_3', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(157, '/t03w_240_3', [47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(158, '/t03w_240_3', [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
	[tc.DownloadFile(159, '/t03w_240_4', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(160, '/t03w_240_4', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(161, '/t03w_240_4', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(162, '/t03w_240_5', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(163, '/t03w_240_5', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(164, '/t03w_240_5', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
	[tc.DownloadFile(165, '/t03w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(166, '/t03w_240_6', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(167, '/t03w_240_6', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(168, '/t03w_240_7', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(169, '/t03w_240_7', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(170, '/t03w_240_7', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(171, '/t03w_240_8', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(172, '/t03w_240_8', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(173, '/t03w_240_9', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(174, '/t04w_240_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(175, '/t04w_240_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(176, '/t04w_240_1', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
	[tc.DownloadFile(177, '/t04w_240_1', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]), Send, WaitMode.Wait],
	[tc.DownloadFile(178, '/t04w_240_2', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(179, '/t04w_240_2', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(180, '/t04w_240_3', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(181, '/t04w_240_4', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(182, '/t04w_240_5', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(183, '/t04w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait]
]