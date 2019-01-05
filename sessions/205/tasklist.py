tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
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
    [tc.DownloadFile(30, '/telemetry.previous', [1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1490, 1540, 1590]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1478, 1528, 1578, 1628, 1678, 1728, 1778]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.current', [10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [2010, 48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.previous', [1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [998, 1048, 1098, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.current', [1998, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.previous', [2002, 2052, 2102, 2152, 2202, 2252, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.current', [972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.current', [1972, 2022, 42, 92, 142, 192, 242, 292, 342, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.previous', [2172, 2222, 2272, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1496]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.current', [942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.current', [1942, 1992, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/telemetry.current', [904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/telemetry.current', [1904, 1954, 2004, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/telemetry.previous', [1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 1508, 1558, 1608, 1658, 1708]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/telemetry.current', [866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/telemetry.current', [1866, 1916, 1966, 2016, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/telemetry.previous', [1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/telemetry.current', [828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/telemetry.current', [1828, 1878, 1928, 1978, 2028]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]