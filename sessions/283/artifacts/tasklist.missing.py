tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1401, 1407, 1413, 1425, 1437, 1451, 1463, 1475, 1487, 1501, 1513, 1525, 1537, 1551, 1563, 1575, 1587]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1601, 1613, 1625, 1637, 1651, 1663, 1675, 1687, 1701, 1713, 1725, 1731, 1737, 1751, 1763, 1775, 1781]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1787, 1801, 1813, 1825, 1831, 1837, 1851, 1863, 1875, 1881, 1887, 1901, 1913, 1925, 1931, 1937, 1951]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1963, 1975, 1981, 1987, 2001, 2013, 2025, 2031, 2037, 2051, 2063, 2075, 2081, 2087, 2101, 2113]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [2125, 2131, 2137, 2151, 2163, 2175, 2181, 2187, 2201, 2213, 2225, 2231, 2237, 2251, 2263, 2275]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [7, 21, 33, 45, 57, 71, 83, 95, 107, 121, 133, 145, 151, 157, 171, 183, 195, 201]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [207, 221, 233, 245, 251, 257, 271, 283, 295, 301, 307, 321, 333, 345, 351, 357, 371, 383]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [395, 401, 407, 421, 433, 445, 451, 457, 471, 483, 495, 501, 507, 521, 533, 545, 551, 557]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [571, 583, 595, 601, 607, 621, 633, 645, 651, 657, 671, 683, 695, 701, 707, 721, 733, 745]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.current', [751, 757, 771, 783, 795, 801, 807, 821, 833, 845, 851, 857, 871, 883, 895, 901, 907, 921]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.current', [933, 945, 951, 957, 971, 983, 995, 1001, 1007, 1021, 1033, 1045, 1051, 1057, 1071, 1083, 1095, 1101]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.current', [1107, 1121, 1133, 1145, 1151, 1157, 1171, 1183, 1195, 1201, 1207, 1221, 1233, 1245, 1251, 1257, 1271, 1283]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.current', [1295, 1301, 1307, 1321, 1333, 1345, 1351, 1357, 1371, 1383, 1395, 1401, 1407, 1421, 1433, 1445, 1451, 1457]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [1471, 1483, 1495, 1501, 1507, 1521, 1533, 1539, 1545, 1551, 1557, 1571, 1583, 1595, 1601, 1607, 1621]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/p3_480_0', [28, 31, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/p3_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait]
]