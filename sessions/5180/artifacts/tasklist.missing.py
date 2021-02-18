tasks = [
[tc.DownloadFile(30, '/telemetry.current', [22, 41, 47, 72, 91, 97, 122, 141, 147, 172, 191, 197, 222, 241, 247]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [253, 259, 272, 297, 303, 322, 347, 353, 372, 397, 409, 422, 447, 472, 522]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [1809, 1821, 1827, 1877, 1883, 1889, 1927, 1939, 1989, 2009, 2039, 2059, 2089, 2095]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [2102, 2109, 2139, 2145, 2152, 2159, 2189, 2195, 2202, 2209, 2239, 2245, 2252, 2259]), Send, WaitMode.Wait]
]