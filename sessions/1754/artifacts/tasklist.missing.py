tasks = [
[tc.DownloadFile(30, '/suns_ps_12', [101, 104, 144, 151, 152, 156, 158, 171, 183, 184, 190, 192, 193, 197, 240]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/suns_ps_12_sec', [98, 105, 111, 113, 114, 129, 171, 172, 173, 174, 176, 178]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/suns_ps_12_sec', [179, 180, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait]
]