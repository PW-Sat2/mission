tasks = [
[tc.DownloadFile(30, '/telemetry.current', [364, 371, 377, 383, 389, 395, 401, 407, 414, 421, 427, 433, 439, 445, 451, 457, 464, 471]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [477, 483, 489, 495, 501, 507, 514, 521, 527, 533, 539, 545, 551, 557, 564, 571, 577, 583]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/p08w_480_0', [37, 45, 47, 48, 53, 54, 57, 90, 91, 168]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/p09w_480_0', [80]), Send, WaitMode.Wait]
]