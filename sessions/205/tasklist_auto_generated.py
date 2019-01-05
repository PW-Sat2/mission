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
    [tc.DownloadFile(30, '/telemetry.previous', [1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1658, 1708, 1758, 1808, 1858, 1908, 1958]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.current', [2003, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [2008, 2058, 2108, 2158, 2208, 2258, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 1670]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.current', [978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.current', [1978, 2028, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.current', [916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.current', [1916, 1966, 2016, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.previous', [1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.current', [890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.current', [1890, 1940, 1990, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.previous', [2040, 2090, 2140, 2190, 2240, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1664, 1714]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.current', [1860, 1910, 1960, 2010, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.current', [822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/telemetry.current', [1822, 1872, 1922, 1972, 2022, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/telemetry.previous', [1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/telemetry.current', [784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/telemetry.current', [1784, 1834, 1884, 1934, 1984, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/telemetry.previous', [2126, 2176, 2226, 2276]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/telemetry.current', [796, 846, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/telemetry.current', [1796, 1846, 1896, 1946, 1996]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]