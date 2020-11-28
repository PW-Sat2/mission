tasks = [
[tc.DownloadFile(30, '/telemetry.current', [169, 176, 182, 188, 194, 200, 206, 212, 219, 226, 232, 238, 244, 250, 256, 262, 269, 276]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [282, 288, 294, 300, 306, 312, 319, 326, 332, 338, 344, 350, 356, 362, 369, 376, 382, 388]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/w_p480_0_0', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171]), Send, WaitMode.Wait]
]