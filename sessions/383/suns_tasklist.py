tasks = [
    # SunS suns_ps_1 experiment file download
    [tc.DownloadFile(21, '/suns_ps_1', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/suns_ps_1', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/suns_ps_1', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/suns_ps_1', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/suns_ps_1', [i for i in range(80, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/suns_ps_1', [i for i in range(100, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/suns_ps_1', [i for i in range(120, 140, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/suns_ps_1', [i for i in range(140, 160, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/suns_ps_1', [i for i in range(160, 180, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/suns_ps_1', [i for i in range(180, 200, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_1', [i for i in range(200, 220, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_1', [i for i in range(220, 240, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_1', [i for i in range(240, 250, 1)]), Send, WaitMode.Wait],
]
