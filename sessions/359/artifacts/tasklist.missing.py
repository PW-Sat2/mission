tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 2150, 2200]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [170, 220, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970]), Send, WaitMode.Wait]
]