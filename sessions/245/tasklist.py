tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

     # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1536, 1586, 1636, 1686]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [31, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 6, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [106, 156, 206, 256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 44, 94, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1974, 2024, 2074, 2124, 2174, 2224, 2274, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998, 2048, 2098, 2148]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794, 1844, 1894, 18, 68, 118, 168, 218]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2198, 2248, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1530, 1580]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068, 1118, 1168, 1218]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1268, 1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 38, 88, 138, 188, 238, 288, 338]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1388, 1438, 1488, 1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 0, 50, 100, 150, 200, 250, 300, 350, 400]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1542, 1592, 1642, 1692, 1742, 1792, 1842]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 12, 62, 112, 162, 212, 262, 312, 362, 412, 462]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 24, 74, 124, 174, 224, 274, 324, 374, 424, 474, 524, 574]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [2154, 2204, 2254]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1624, 1674, 1724, 1774, 1824, 1874]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    ["The next step after beacon is files remove.", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(101, '/p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, '/p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(103, '/p5_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]