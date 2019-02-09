tasks = [
    # Generated on 2019-02-09 19:21:56.825000, contains telemetry from sessions 431 to 438.
    # The session starts on 2019-02-09 20:38:05+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2171, 2221, 2271, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 16, 66, 116, 166, 216, 266, 316, 366, 416]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2046, 2096, 2146, 2196, 2246, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [466, 516, 566, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 28, 78, 128, 178, 228]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1934, 1984, 2034, 2084, 2134, 2184, 2234, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558, 1608, 1658, 1708, 1758, 1808]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [278, 328, 378, 428, 478, 528, 48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 10, 60, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 190, 240, 290, 340, 390, 440, 490, 540]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 202, 252, 302, 352, 402, 452]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [160, 210, 260, 310, 360, 410, 460, 510, 560, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402, 1452]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 214, 264, 314, 364]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]