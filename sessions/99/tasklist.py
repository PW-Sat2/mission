tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 98 and 99
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(470, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(476, 670, 12)]), Send, WaitMode.Wait],

    # Sixth SunS experiment
    [tc.PerformSunSExperiment(12, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_6'), Send, WaitMode.Wait],

    # More telemetry between session 98 and 99
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(473, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(479, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(471, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(23, '/telemetry.current', [i for i in range(472, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.current', [i for i in range(474, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(25, '/telemetry.current', [i for i in range(475, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.current', [i for i in range(477, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.current', [i for i in range(478, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.current', [i for i in range(480, 670, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(29, '/telemetry.current', [i for i in range(481, 670, 12)]), Send, WaitMode.Wait],

    # More telemetry between session 96 and 98
    [tc.DownloadFile(40, '/telemetry.previous', [i for i in range(1893, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [i for i in range(1899, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [i for i in range(1891, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [i for i in range(1892, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(3, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(9, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(15, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(21, 470, 25)]), Send, WaitMode.Wait],

    [tc.DownloadFile(44, '/telemetry.previous', [i for i in range(1894, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [i for i in range(1895, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [i for i in range(1897, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [i for i in range(1898, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [i for i in range(1900, 2280, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [i for i in range(1901, 2280, 12)]), Send, WaitMode.Wait],

    [tc.DownloadFile(54, '/telemetry.current', [i for i in range(27, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [i for i in range(30, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [i for i in range(33, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [i for i in range(40, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [i for i in range(46, 470, 25)]), Send, WaitMode.Wait],

    # Much more telemetry between session 96 and 98
    [tc.DownloadFile(60, '/telemetry.current', [i for i in range(1, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [i for i in range(2, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [i for i in range(4, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [i for i in range(5, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [i for i in range(7, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [i for i in range(8, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [i for i in range(10, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [i for i in range(11, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [i for i in range(13, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.current', [i for i in range(14, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.current', [i for i in range(16, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [i for i in range(17, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [i for i in range(19, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [i for i in range(20, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [i for i in range(22, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [i for i in range(23, 470, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [i for i in range(24, 470, 25)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
