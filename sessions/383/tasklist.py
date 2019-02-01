tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(10, '/telemetry.previous', [2231, 2256, 2244, 2268, 2238, 2250, 2262, 2274]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [1, 51, 101, 151, 26, 76, 126, 14, 64, 114, 164, 38, 88, 138, 8, 58, 108, 158, 20, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(12, '/telemetry.current', [120, 170, 32, 82, 132, 44, 94, 144]), Send, WaitMode.Wait],
    # auto-generated telemetry end

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

    [tc.DownloadFile(40, '/suns_ps_1_sec', [i for i in range(0, 25, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_1_sec', [i for i in range(25, 50, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_1_sec', [i for i in range(50, 75, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_1_sec', [i for i in range(75, 100, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_1_sec', [i for i in range(100, 125, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_1_sec', [i for i in range(125, 150, 1)]), Send, WaitMode.Wait],

    # SunS suns_ps_1_sec experiment file download
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]