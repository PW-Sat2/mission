tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1399, 1449, 1499, 1549, 1811, 1899, 1911, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [269]), Send, WaitMode.Wait]
]