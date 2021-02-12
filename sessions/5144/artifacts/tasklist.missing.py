tasks = [
[tc.DownloadFile(30, '/telemetry.current', [7, 19, 31, 57, 69, 81, 107, 119, 131, 157, 169, 181, 207, 219, 231, 257, 269]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [281, 307, 319, 331, 357, 369, 381, 407, 419, 431, 445, 457, 469, 481, 507, 519]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [531, 557, 569, 581, 607, 619, 631, 657, 669, 681, 707, 719, 731, 757, 769, 781]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1861, 1911, 1961, 2011, 2025, 2037, 2049, 2061, 2099, 2111, 2149, 2161, 2199, 2211, 2249, 2261]), Send, WaitMode.Wait]
]