tasks = [
    # Generated on 2019-02-22 15:29:17.371000, contains telemetry from sessions 516 to 523.
    # The session starts on 2019-02-22 21:38:22+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2265, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 10, 60, 110, 160, 210, 260, 310]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2240, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [360, 410, 460, 510, 560, 610, 660, 48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2228, 2278, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2202, 2252, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 42, 92, 142, 192, 242, 292, 342]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2172, 2222, 2272, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [392, 442, 492, 542, 592, 642, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 604, 654]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2134, 2184, 2234, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 1096]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2146, 2196, 2246, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 908, 958, 1008, 1058, 1108]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 28, 78, 128, 178, 228, 278, 328]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [2158, 2208, 2258]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [378, 428, 478, 528, 578, 628]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.RemoveFile(200, 'radfet_8' ), Send, WaitMode.NoWait],
    
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]