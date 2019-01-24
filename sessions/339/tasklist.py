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

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1820]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2027, 2077, 2127, 2177, 2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [802, 852, 902, 952, 1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1814, 1864]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 14, 64, 114, 164, 214, 264, 314]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1364, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 34, 84, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 1838, 1888]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [2184, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1996, 2046, 2096, 2146, 2196, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1938, 1988, 2038, 2088, 2138, 2188, 2238, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558, 1608, 1658, 1708]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]