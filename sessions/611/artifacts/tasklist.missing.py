tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [221, 233, 283, 321, 333, 371, 383, 433, 471, 483, 521, 533, 571, 583, 633, 683, 733]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1259, 1271, 1283, 1333, 1383, 1433]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1483, 1533, 1583, 1621, 1633, 1659, 1671, 1683, 1721, 1733, 1759, 1771, 1783, 1821, 1833, 1871]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1883, 1921, 1933, 1971, 1983, 2021, 2033, 2071, 2083, 2121, 2133, 2171, 2183, 2221, 2233, 2271]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [3, 41, 53, 79, 91, 103, 129, 141, 153, 179, 191, 203, 229, 241, 253, 279, 291]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [303, 329, 341, 353, 379, 391, 403, 429, 441, 453, 479, 491, 503, 529, 541, 553, 579]), Send, WaitMode.Wait]
]