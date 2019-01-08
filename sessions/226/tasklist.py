tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1937, 1987, 2037, 2087, 2137, 2187, 2237]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 32, 82, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1962, 2012, 2062, 2112, 2162, 2212, 2262, 450, 500, 550, 600, 650, 700]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 20, 70, 120, 170, 220, 270]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 474, 524, 574, 624, 674, 724, 774, 824, 874]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 44, 94, 144, 194, 244, 294, 344, 394, 444]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [494, 544, 594, 644, 694, 744, 794, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2044, 2094, 2144, 2194, 2244, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [664, 714, 764, 814, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2206, 2256, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068, 1118, 1168, 1218, 1268, 1318]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [826, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 0, 50, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 480]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080, 1130, 1180, 1230, 1280, 1330, 1380, 1430, 1480]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]