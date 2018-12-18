tasks = [
    [[tc.SetBitrate(3, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    # Telemetry between sessions 91 and 92
    [tc.DownloadFile(10, '/telemetry.current', [i for i in range(107, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(11, '/telemetry.current', [i for i in range(119, 300, 15)]), Send, WaitMode.Wait],

    # Fifth SunS experiment
    [tc.PerformSunSExperiment(20, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_5'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    # More telemetry between sessions 91 and 92
    [tc.DownloadFile(30, '/telemetry.current', [i for i in range(109, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [i for i in range(111, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [i for i in range(113, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [i for i in range(115, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [i for i in range(117, 300, 15)]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [i for i in range(121, 300, 15)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],

    [tc.DownloadFile(100, '/telemetry.previous', [i for i in range(1520, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [i for i in range(1521, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [i for i in range(1522, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [i for i in range(1523, 2280, 40)]), Send, WaitMode.Wait],

    # Download missing photos chunks
    [tc.DownloadFile(40, '/p4_480_0', [22]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p17_480_0', [12, 15, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p18_480_0', [0, 1, 19, 22, 39, 42]), Send, WaitMode.Wait],

    # more telemetry previous chunks 89 - 91
    [tc.DownloadFile(104, '/telemetry.previous', [i for i in range(1524, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [i for i in range(1525, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.previous', [i for i in range(1526, 2280, 40)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(107, '/telemetry.previous', [i for i in range(1527, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [i for i in range(1528, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [i for i in range(1529, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [i for i in range(1530, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.previous', [i for i in range(1531, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [i for i in range(1532, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.previous', [i for i in range(1533, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [i for i in range(1534, 2280, 40)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(115, '/telemetry.previous', [i for i in range(1535, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/telemetry.previous', [i for i in range(1536, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.previous', [i for i in range(1537, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.previous', [i for i in range(1538, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/telemetry.previous', [i for i in range(1539, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/telemetry.previous', [i for i in range(1540, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/telemetry.previous', [i for i in range(1541, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/telemetry.previous', [i for i in range(1542, 2280, 40)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(123, '/telemetry.previous', [i for i in range(1543, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/telemetry.previous', [i for i in range(1544, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/telemetry.previous', [i for i in range(1545, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/telemetry.previous', [i for i in range(1546, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.previous', [i for i in range(1547, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/telemetry.previous', [i for i in range(1548, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.previous', [i for i in range(1549, 2280, 40)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(130, '/telemetry.previous', [i for i in range(1550, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/telemetry.previous', [i for i in range(1551, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/telemetry.previous', [i for i in range(1552, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/telemetry.previous', [i for i in range(1554, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/telemetry.previous', [i for i in range(1555, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/telemetry.previous', [i for i in range(1556, 2280, 40)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(136, '/telemetry.previous', [i for i in range(1557, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/telemetry.previous', [i for i in range(1558, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/telemetry.previous', [i for i in range(1559, 2280, 40)]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/telemetry.previous', [i for i in range(1560, 2280, 40)]), Send, WaitMode.Wait],

    [tc.DownloadFile(140, '/telemetry.current', [i for i in range(0, 112, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/telemetry.current', [i for i in range(2, 112, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/telemetry.current', [i for i in range(4, 112, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/telemetry.current', [i for i in range(6, 112, 10)]), Send, WaitMode.Wait],
    [tc.DownloadFile(144, '/telemetry.current', [i for i in range(8, 112, 10)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
