tasks = [
[tc.DownloadFile(30, '/telemetry.current', [3, 9, 15, 21, 27, 34, 41, 47, 53, 59, 65, 71, 77, 84, 91, 97, 103, 109]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [115, 121, 127, 134, 141, 147, 153, 159, 165, 171, 177, 184, 191, 197, 203, 209, 215, 221]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [227, 234, 241, 247, 253, 259, 265, 271, 277, 284, 291, 297, 303, 309, 315, 321, 327, 334]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [341, 347, 353, 359, 365, 371, 377, 384, 391, 397, 403, 409, 415, 421, 427, 434, 441, 447]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [453, 459, 465, 471, 477, 484, 491, 497, 503, 509, 515, 521, 527, 534, 541, 547, 553]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.previous', [1364, 1371, 1377, 1383, 1389, 1395, 1401, 1407, 1414, 1421, 1427, 1433, 1439, 1445, 1451, 1457, 1464, 1471, 1477]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.previous', [1483, 1489, 1495, 1501, 1507, 1514, 1521, 1527, 1533, 1539, 1545, 1551, 1557, 1564, 1571, 1577, 1583, 1589, 1595]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.previous', [1601, 1607, 1614, 1621, 1627, 1633, 1639, 1645, 1651, 1657, 1664, 1671, 1677, 1683, 1689, 1695, 1701, 1707, 1714]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.previous', [1721, 1727, 1733, 1739, 1745, 1751, 1757, 1764, 1771, 1777, 1783, 1789, 1795, 1801, 1807, 1814, 1821, 1827]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.previous', [1833, 1839, 1845, 1851, 1857, 1864, 1871, 1877, 1883, 1889, 1895, 1901, 1907, 1914, 1921, 1927, 1933, 1939]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.previous', [1945, 1951, 1957, 1964, 1971, 1977, 1983, 1989, 1995, 2001, 2007, 2014, 2021, 2027, 2033, 2039, 2045, 2051]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.previous', [2057, 2064, 2071, 2077, 2083, 2089, 2095, 2101, 2107, 2114, 2121, 2127, 2133, 2139, 2145, 2151, 2157, 2164]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.previous', [2171, 2177, 2183, 2189, 2195, 2201, 2207, 2214, 2221, 2227, 2233, 2239, 2245, 2251, 2257, 2264, 2271, 2277]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/m9n_480_0', [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/m9w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/m4n_480_0', [24, 27, 28, 30, 31, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/m4n_480_0', [45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/m4n_480_0', [62, 63, 64, 65, 67, 70, 71, 87, 89, 94, 95, 97, 98, 100, 103, 104]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/m4w_480_0', [20, 21, 22, 23, 24, 25, 26, 28, 29, 30, 32, 34, 35, 36, 39, 40, 41, 43]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/m4w_480_0', [44, 49, 52, 53, 54, 56, 59, 61, 63, 64, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/m4w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/m4w_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/m5n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/m5n_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/m5n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/m5w_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/m5w_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/m5w_480_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
	[tc.DownloadFile(58, '/m5w_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
	[tc.DownloadFile(59, '/m6n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
	[tc.DownloadFile(60, '/m6n_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
	[tc.DownloadFile(61, '/m6n_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]), Send, WaitMode.Wait],
	[tc.DownloadFile(62, '/m6w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(63, '/m6w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
	[tc.DownloadFile(64, '/m6w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]), Send, WaitMode.Wait],
	[tc.DownloadFile(65, '/m6w_480_0', [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
	[tc.DownloadFile(66, '/m6w_480_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
	[tc.DownloadFile(67, '/m6w_480_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
	[tc.DownloadFile(68, '/m6w_480_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
	[tc.DownloadFile(69, '/m7n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
	[tc.DownloadFile(70, '/m7n_480_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
	[tc.DownloadFile(71, '/m7n_480_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
	[tc.DownloadFile(72, '/m7w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
	[tc.DownloadFile(73, '/m7w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
	[tc.DownloadFile(74, '/m7w_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
	[tc.DownloadFile(75, '/m7w_480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
	[tc.DownloadFile(76, '/m7w_480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
	[tc.DownloadFile(77, '/m7w_480_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
	[tc.DownloadFile(78, '/m7w_480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145]), Send, WaitMode.Wait],
	[tc.DownloadFile(79, '/m7w_480_0', [146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
	[tc.DownloadFile(80, '/m8n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
	[tc.DownloadFile(81, '/m8n_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(82, '/m8n_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
	[tc.DownloadFile(83, '/m8w_480_0', [7, 8, 9, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
	[tc.DownloadFile(84, '/m8w_480_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
	[tc.DownloadFile(85, '/m8w_480_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
	[tc.DownloadFile(86, '/m8w_480_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
	[tc.DownloadFile(87, '/m8w_480_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
	[tc.DownloadFile(88, '/m8w_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
	[tc.DownloadFile(89, '/m8w_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
	[tc.DownloadFile(90, '/m8w_480_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]), Send, WaitMode.Wait],
	[tc.DownloadFile(91, '/m8w_480_0', [154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
	[tc.DownloadFile(92, '/m9n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
	[tc.DownloadFile(93, '/m9n_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(94, '/m9n_480_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]), Send, WaitMode.Wait],
	[tc.DownloadFile(95, '/m9n_480_0', [66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
	[tc.DownloadFile(96, '/m9w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
	[tc.DownloadFile(97, '/m9w_480_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
	[tc.DownloadFile(98, '/m9w_480_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
	[tc.DownloadFile(99, '/m9w_480_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
	[tc.DownloadFile(100, '/m9w_480_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
	[tc.DownloadFile(101, '/m9w_480_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
	[tc.DownloadFile(102, '/m9w_480_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait]
]