tasks = [
[tc.DownloadFile(30, '/telemetry.current', [21, 33, 71, 83, 121, 133, 171, 183, 221, 233, 271, 283, 321, 333, 371, 383]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [421, 433, 471, 483, 521, 533, 571, 583, 621, 633, 671, 683, 721, 733, 771]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [783, 821, 833, 871, 883, 921, 933, 971, 983, 1021, 1033, 1071, 1083, 1109, 1121]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [1133, 1159, 1171, 1183, 1209, 1221, 1233, 1259, 1271, 1283, 1309, 1321, 1333, 1359, 1371]), Send, WaitMode.Wait]
]