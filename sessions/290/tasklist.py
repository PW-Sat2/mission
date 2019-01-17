tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773, 823, 873, 923, 973]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2228, 2278, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1790, 1840, 1890, 1940, 1990, 2040, 2090]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1048, 1098, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 10, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2140, 2190, 2240, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1772, 1822, 1872, 1922, 1972, 2022]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 30, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1130, 1180, 1230, 1280, 1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 42, 92, 142]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2072, 2122, 2172, 2222, 2272, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1796, 1846, 1896, 1946, 1996]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [192, 242, 292, 342, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 4, 54, 104, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [204, 254, 304, 354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 16, 66, 116, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2046, 2096, 2146, 2196, 2246]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]