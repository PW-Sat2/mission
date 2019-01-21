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
    [tc.DownloadFile(30, '/telemetry.previous', [733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 758, 808, 858, 908, 958, 1008, 1058, 1108, 1158]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2208, 2258, 746, 796, 846, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 16, 66, 116, 166, 216, 266, 316]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 770, 820, 870, 920, 970, 1020, 1070]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 40]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2120, 2170, 2220, 2270, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1090, 1140, 1190, 1240, 1290, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 752, 802, 852, 902, 952]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 22, 72, 122, 172, 222, 272, 322, 372, 422]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2002, 2052, 2102, 2152, 2202, 2252, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 34, 84, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 776, 826, 876]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1184, 1234, 1284, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [926, 976, 1026, 1076, 1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]