tasks = [
[tc.DownloadFile(30, '/telemetry.current', [650, 707, 725, 737, 775, 787, 794, 825, 837, 844, 857, 875, 887, 894, 901]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [925, 937, 969, 975, 987, 1001, 1025, 1037, 1063, 1075, 1087, 1113, 1125, 1137, 1163]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1175, 1187, 1213, 1225, 1237, 1263, 1275, 1287, 1313, 1325, 1337, 1363, 1375, 1387]), Send, WaitMode.Wait]
]