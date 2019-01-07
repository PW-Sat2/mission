tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [95, 119, 145, 169, 195, 219, 245, 257, 269, 295, 307, 319, 345, 357, 369, 395, 407, 419]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [445, 457, 469, 495, 507, 519, 545, 557, 569, 595, 607, 619, 645, 657, 669, 695, 707, 719]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [745, 757, 769, 795, 807, 819, 845, 857, 869, 895, 907, 919, 945, 957, 969, 995, 1007, 1019]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1045, 1057, 1069, 1095, 1107, 1119, 1157, 1169, 1207, 1219, 1257, 1269, 1307, 1319, 1333, 1357, 1369, 1383]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [1407, 1419, 1457, 1469, 1507, 1519, 1557, 1569, 1607, 1619, 1633, 1657, 1669, 1683, 1707, 1719, 1733, 1745]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.previous', [1757, 1769, 1783, 1807, 1819, 1857, 1869, 1883, 1895, 1907, 1919, 1933, 1945, 1957, 1969, 1983, 1995, 2007]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.previous', [2019, 2033, 2057, 2069, 2083, 2107, 2119, 2133, 2145, 2157, 2169, 2183, 2207, 2219, 2233, 2257, 2269]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [15, 39, 65, 77, 89, 103, 127, 139, 153, 165, 177, 189, 203, 227]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [239, 265, 277, 289, 303, 327, 339, 353, 377, 389, 403, 427, 439]), Send, WaitMode.Wait]
]