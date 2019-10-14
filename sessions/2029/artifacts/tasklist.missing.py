tasks = [
[tc.DownloadFile(30, '/telemetry.current', [4, 10, 17, 24, 30, 36, 42, 48, 54, 60, 67, 74, 80, 86]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [2147, 2154, 2160, 2166, 2172, 2178, 2184, 2190, 2197, 2204, 2210]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [2216, 2222, 2228, 2234, 2240, 2247, 2254, 2260, 2266, 2272, 2278]), Send, WaitMode.Wait]
]