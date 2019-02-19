tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1605, 1705, 1955, 2105, 2205]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [49, 99, 149, 199, 249, 275, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1463, 1499, 1513, 1549, 1563, 1599, 1649, 1699]), Send, WaitMode.Wait]
]