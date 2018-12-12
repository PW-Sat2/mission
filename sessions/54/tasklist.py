tasks = [
    [[tc.SetBitrate(10, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(11, '/'), Send, WaitMode.Wait],

    # Telemetry download between session 53 and 54
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(570, 770, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(595, 770, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(582, 770, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(607, 770, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(576, 770, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(588, 770, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(601, 770, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(613, 770, 50)]), Send, WaitMode.Wait],

    # SunS experiment secondary file
    [tc.DownloadFile(30, '/suns_2_sec', [i for i in range(0, 10, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_2_sec', [i for i in range(10, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_2_sec', [i for i in range(20, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_2_sec', [i for i in range(30, 40, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(34, '/suns_2_sec', [i for i in range(40, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_2_sec', [i for i in range(50, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_2_sec', [i for i in range(60, 70, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_2_sec', [i for i in range(70, 80, 1)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(38, '/suns_2_sec', [i for i in range(80, 90, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_2_sec', [i for i in range(90, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_2_sec', [i for i in range(100, 110, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_2_sec', [i for i in range(110, 120, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_2_sec', [i for i in range(120, 125, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]
