tasks = [
    [[tc.SetBitrate(3, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between sessions 91 and 92
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(107, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(119, 300, 15)]), Send, WaitMode.Wait],

    # Fifth SunS experiment
    [tc.PerformSunSExperiment(20, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_5'), Send, WaitMode.Wait],

    # More telemetry between sessions 91 and 92
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(109, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(111, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(113, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(115, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(117, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(121, 300, 15)]), Send, WaitMode.Wait],

    # Download missing photos chunks
    [tc.DownloadFile(40, '/p4_480_0', [22]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p17_480_0', [12, 15, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p18_480_0', [0, 1, 19, 22, 39, 42]), Send, WaitMode.Wait],

    # Photos to download

    # more telemetry previous chunks
    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(1712, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [i for i in range(1714, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [i for i in range(1716, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [i for i in range(1718, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.previous', [i for i in range(1720, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [i for i in range(1722, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.previous', [i for i in range(1724, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [i for i in range(1726, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [i for i in range(1728, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [i for i in range(1730, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [i for i in range(1732, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.previous', [i for i in range(1734, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [i for i in range(1736, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.previous', [i for i in range(1738, 2280, 30)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [i for i in range(1740, 2280, 30)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
