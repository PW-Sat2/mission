tasks = [
    # Generated on 2019-02-10 19:24:51.319000, contains telemetry from sessions 439 to 445.
    # The session starts on 2019-02-10 20:42:48+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 728, 778, 828, 878, 928, 978, 1028, 1078]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773, 823, 873, 923, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2128, 2178, 2228, 2278, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 36, 86, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 740, 790, 840, 890]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 10, 60, 110, 160, 210]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1940, 1990, 2040, 2090, 2140, 2190, 2240, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 30, 80, 130, 180, 230, 280]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 722]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [330, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 42, 92, 142, 192, 242, 292, 342, 392]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172, 2222, 2272, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [2184, 2234, 746, 796, 846, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [504, 554, 604, 654, 704, 754, 804, 854, 904, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [566, 616, 666, 716, 766, 816, 866, 916]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]