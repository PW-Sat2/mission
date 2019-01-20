tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [1459, 1509, 1559, 1609, 1659, 1484, 1534, 1584, 1634, 1472, 1522, 1572, 1622, 1672, 1496, 1546, 1596, 1646, 1466, 1516]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1566, 1616, 1666, 1478, 1528, 1578, 1628, 1678, 1490, 1540, 1590, 1640, 1502, 1552, 1602, 1652]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(60, '/p1_128_0', [i for i in range(0, 14, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_128_0', [i for i in range(14, 28, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p2_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p2_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p3_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p3_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(66, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p4_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(68, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p5_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/p6_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p6_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(72, '/p7_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p7_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(74, '/p8_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p8_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(76, '/p9_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p9_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(78, '/p10_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p10_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]