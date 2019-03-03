tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1512, 2180]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [420, 470, 520, 570, 620, 670, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170]), Send, WaitMode.Wait]
]