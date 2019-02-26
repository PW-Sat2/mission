tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1561, 1573, 1611, 1623, 1661, 1673, 1711, 1723, 1761, 1773, 1799, 1811, 1823, 1849]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1861, 1873, 1899, 1911, 1923, 1949, 1961, 1973, 1999, 2011, 2023, 2049, 2061]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [2073, 2099, 2111, 2123, 2149, 2161, 2173, 2199, 2211, 2223, 2249, 2261, 2273]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [31, 43, 81, 93, 131, 143, 181, 193, 231, 243, 281, 293, 319, 331, 343, 369, 381, 393, 419]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [431, 443, 469, 481, 493, 519, 531, 543, 569, 581, 593, 619, 631, 643, 669, 681, 693, 719, 731]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [743, 769, 781, 793, 819, 831, 843, 869, 881, 893, 919, 931, 943, 969, 981, 993, 1019, 1031]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [1043, 1069, 1081, 1093, 1119, 1131, 1143, 1169, 1181, 1193, 1219, 1231, 1243, 1269, 1281, 1293, 1319, 1331]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [1343, 1369, 1381, 1393, 1419, 1431, 1443, 1469, 1481, 1487, 1493, 1519, 1531, 1543, 1569, 1581, 1593, 1619]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [1631, 1643, 1669, 1681, 1693, 1719, 1731, 1743, 1769, 1781, 1793, 1819, 1831, 1843, 1869, 1881, 1893, 1919]), Send, WaitMode.Wait]
]