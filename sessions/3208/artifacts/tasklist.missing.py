tasks = [
[tc.DownloadFile(30, '/telemetry.current', [24, 36, 48, 74, 86, 98, 112, 124, 136, 148, 162, 174, 186, 198, 212, 224]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/p1_480_0', [56, 57, 58, 59, 60, 61, 62, 63, 83, 85, 86, 90, 91, 92, 93, 97, 98]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p1_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p1_480_0', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/p1_480_0', [134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150]), Send, WaitMode.Wait]
]