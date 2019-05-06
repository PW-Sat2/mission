tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1747, 1754, 1760, 1766, 1772, 1778, 1784, 1790, 1797, 1804, 1810, 1816, 1822, 1828, 1834, 1840, 1847, 1854]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1860, 1866, 1872, 1878, 1884, 1890, 1897, 1904, 1910, 1916, 1922, 1928, 1934, 1940, 1947, 1954, 1960]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1966, 1972, 1978, 1984, 1990, 1997, 2004, 2010, 2016, 2022, 2028, 2034, 2040, 2047, 2054, 2060, 2066]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [2072, 2078, 2084, 2090, 2097, 2104, 2110, 2116, 2122, 2128, 2134, 2140, 2147, 2154, 2160, 2166, 2172]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [2178, 2184, 2190, 2197, 2204, 2210, 2216, 2222, 2228, 2234, 2240, 2247, 2254, 2260, 2266, 2272, 2278]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/p4_480_0', [8, 11, 16, 17, 18, 21, 23, 41, 42, 43, 44, 45, 46, 49, 116, 117]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/p4_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/p7_480_0', [71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/p7_480_0', [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/p7_480_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/p7_480_0', [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.current', [4, 10, 17, 24, 30, 36, 42, 48, 54, 60, 67, 74, 80, 86, 92, 98, 104, 110, 117, 124]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.current', [130, 136, 142, 148, 154, 160, 167, 174, 180, 186, 192, 198, 204, 210, 217, 224, 230, 236, 242, 248]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [254, 260, 267, 274, 280, 286, 292, 298, 304, 310, 317, 324, 330, 336, 342, 348, 354, 360, 367]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.current', [374, 380, 386, 392, 398, 404, 410, 417, 424, 430, 436, 442, 448, 454, 460, 467, 474, 480, 486]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.current', [492, 498, 504, 510, 517, 524, 530, 536, 542, 548, 554, 560, 567, 574, 580, 586, 592, 598, 604]), Send, WaitMode.Wait]
]