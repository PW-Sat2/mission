tasks = [
[tc.DownloadFile(30, '/telemetry.current', [1548, 1596, 1644, 1653, 1656, 1665, 1716]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/t05w_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/t09w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 114, 115]), Send, WaitMode.Wait]
]