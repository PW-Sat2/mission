tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [2058, 2065, 2071, 2077, 2083, 2089, 2095, 2101, 2108, 2115, 2121, 2127, 2133, 2139, 2145, 2151, 2158, 2165]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [2171, 2177, 2183, 2189, 2195, 2201, 2208, 2215, 2221, 2227, 2233, 2239, 2245, 2251, 2258, 2265, 2271, 2277]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [3, 9, 15, 21, 28, 35, 41, 47, 53, 59, 65, 71, 78, 85, 91, 97, 103, 109, 115, 121]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [128, 135, 141, 147, 153, 159, 165, 171, 178, 185, 191, 197, 203, 209, 215, 221, 228, 235, 241, 247]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [253, 259, 265, 271, 278, 285, 291, 297, 303, 309, 315, 321, 328, 335, 341, 347, 353, 359, 365, 371]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [378, 385, 391, 397, 403, 409, 415, 421, 428, 435, 441, 447, 453, 459, 465, 471, 478, 485, 491, 497]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [503, 509, 515, 521, 528, 535, 541, 547, 553, 559, 565, 571, 578, 585, 591, 597, 603, 609, 615]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [621, 628, 635, 641, 647, 653, 659, 665, 671, 678, 685, 691, 697, 703, 709, 715, 721, 728, 735]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [741, 747, 753, 759, 765, 771, 778, 785, 791, 797, 803, 809, 815, 821, 828, 835, 841, 847, 853]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.current', [859, 865, 871, 878, 885, 891, 897, 903, 909, 915, 921, 928, 935, 941, 947, 953, 959, 965, 971]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.current', [978, 985, 991, 997, 1003, 1009, 1015, 1021, 1028, 1035, 1041, 1047, 1053, 1059, 1065, 1071, 1078, 1085, 1091]), Send, WaitMode.Wait]
]