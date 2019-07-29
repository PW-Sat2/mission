tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1721, 1728, 1734, 1740, 1746, 1758, 1771, 1778, 1784, 1790, 1796, 1808, 1821, 1828, 1834, 1840, 1846, 1858, 1878]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1884, 1896, 1908, 1928, 1934, 1946, 1958, 1978, 1984, 1996, 2008, 2021, 2028, 2034, 2046, 2058, 2071, 2078, 2084]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [2096, 2108, 2121, 2128, 2134, 2146, 2158, 2171, 2178, 2184, 2196, 2208, 2228, 2234, 2246, 2258, 2271, 2278]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [4, 16, 28, 34, 41, 54, 66, 78, 84, 91, 104, 116, 128, 134, 141, 154]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [166, 178, 184, 191, 204, 216, 228, 234, 241, 254, 266, 278, 284, 291, 304, 316]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [328, 334, 341, 354, 366, 378, 384, 391, 404, 416, 428, 434, 441, 454, 466, 478]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [484, 491, 504, 516, 522, 528, 534, 541, 554, 566, 572, 578, 584, 591, 604, 616]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [622, 628, 634, 641, 654, 666, 672, 678, 684, 691, 704, 716, 722, 728, 734, 741]), Send, WaitMode.Wait]
]