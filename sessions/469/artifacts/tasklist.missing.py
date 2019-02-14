tasks = [
[tc.DownloadFile(30, '/telemetry.previous', [1571, 1621, 1659, 1671, 1709, 1721, 1759, 1771, 1809, 1821, 1859, 1871, 1909, 1921, 1959, 1971]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [15, 33, 133, 147, 183, 233, 265, 283, 333, 377, 383, 465, 471, 483]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [521, 533, 571, 577, 583, 633, 653, 683, 733, 777, 783, 833, 865]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [883, 921, 933, 965, 971, 983, 1021, 1033, 1040, 1071, 1083, 1121, 1133]), Send, WaitMode.Wait]
]