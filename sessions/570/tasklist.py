tasks = [
    # Generated on 2019-03-01 16:41:41.073000, contains telemetry from sessions 565 to 570.
    # The session starts on 2019-03-01 20:34:49+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 524, 574, 624, 674]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 44, 94, 144, 194, 244]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574, 1624, 1674]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 512, 562, 612, 662, 712, 762, 812, 862]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [294, 344, 394, 444, 494, 544, 594, 644, 694, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036, 1086]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [582, 632, 682, 6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 26, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2136, 2186, 2236, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 518]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 38, 88, 138, 188, 238, 288, 338, 388]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068, 1118, 1168, 1218, 1268, 1318, 1368, 1418, 1468, 1518]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 530, 580, 630, 680, 730]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [438, 488, 538, 588, 638, 688, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [780, 830, 880, 930, 980, 1030, 1080, 1130, 1180, 1230, 1280, 1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [700, 12, 62, 112, 162, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662, 712]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [2042, 2092, 2142, 2192, 2242]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]