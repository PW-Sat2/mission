tasks = [
    # Generated on 2019-02-18 13:52:53.051000, contains telemetry from sessions 493 to 497.
    # The session starts on 2019-02-18 19:46:29+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove files
    [tc.RemoveFile(100, 'p1_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, 'p1_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, 'p2_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, 'p2_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, 'p3_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(105, 'p3_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, 'p4_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(107, 'p4_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, 'p5_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(109, 'p5_480_0' ), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(110, 'p6_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(111, 'p6_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(112, 'p7_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(113, 'p7_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(114, 'p8_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(115, 'p8_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(116, 'p9_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(117, 'p9_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(118, 'p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(119, 'p10_480_0'), Send, WaitMode.NoWait],

    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1013, 1063, 1113, 1163, 1213, 1263, 1313, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 26, 76, 126, 176, 226, 276]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176, 1226, 1276]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1326, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1300]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1312]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 32, 82, 132, 182, 232]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1324]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1282, 1332, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1374, 1424, 1474, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 1336]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove files - try again, expect errors if first try succeeded
    [tc.RemoveFile(120, 'p10_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(121, 'p10_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(122, 'p9_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(123, 'p9_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(124, 'p8_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(125, 'p8_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(126, 'p7_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(127, 'p7_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(128, 'p6_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(129, 'p6_128_0' ), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.RemoveFile(130, 'p5_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(131, 'p5_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(132, 'p4_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(133, 'p4_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(134, 'p3_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(135, 'p3_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(136, 'p2_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(137, 'p2_128_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(138, 'p1_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(139, 'p1_128_0' ), Send, WaitMode.NoWait],

    [tc.ListFiles(4, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]