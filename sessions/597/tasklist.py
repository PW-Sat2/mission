tasks = [
    # Generated on 2019-03-05 19:31:33.439000, contains telemetry from sessions 590 to 597.
    # The session starts on 2019-03-05 20:51:57+01:00.

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
    [tc.DownloadFile(50, '/telemetry.previous', [2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.previous', [1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2226, 2276, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1788, 1838, 1888, 1938, 1988, 2038, 2088]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2138, 2188, 2238, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1770, 1820, 1870, 1920, 1970, 2020]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [2070, 2120, 2170, 2220, 2270, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1794, 1844, 1894, 1944, 1994]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2021, 2071, 2121, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1896, 1946, 1996, 2046, 2096, 2146, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [558, 608, 658, 708, 758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 28, 78, 128, 178, 228, 278, 328, 378]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 40, 90, 140, 190, 240]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1102, 1152, 1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [2102, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [964, 1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1964, 2014, 2064, 2114]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.RemoveFile(110, 'suns_ps_2'), Send, WaitMode.NoWait],
    [tc.RemoveFile(110, 'suns_ps_2_sec'), Send, WaitMode.NoWait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]