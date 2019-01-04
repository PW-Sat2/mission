tasks = [
[tc.DownloadFile(30, '/telemetry.current', [24,72,120,168,216,264,312,360,408,456,504,552,600,648,654,696,]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [744,792,840,888,936,984,1032,1080,1128,1176,1224,1272,1320,1368,1416]), Send, WaitMode.Wait]
]