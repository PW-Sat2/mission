tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1829]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [49, 99, 149, 199, 249, 299, 349, 399, 449, 499, 537, 549, 587, 599, 637, 649]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [687, 699, 737, 749, 787, 799, 837, 849, 887, 899, 937, 949, 987, 999, 1037, 1049]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [1087, 1099, 1137, 1149, 1187, 1199, 1237, 1249, 1287, 1299, 1349, 1399, 1437, 1487, 1537]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [1549, 1587, 1599, 1637, 1687, 1737, 1749, 1787, 1837, 1887, 1937, 1949, 1987, 2037, 2049]), Send, WaitMode.Wait]
]