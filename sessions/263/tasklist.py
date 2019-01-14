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
    [tc.DownloadFile(30, '/telemetry.previous', [311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [31, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 6, 56, 106, 156, 206, 256]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 324]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [306, 356, 406, 456, 506, 556, 606, 656, 706, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1374, 1424, 1474, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 348]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [594, 644, 694, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 38, 88, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248, 1298, 1348]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248, 318, 368]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918, 968, 1018, 1068, 1118, 1168, 1218, 1268, 1318, 1368]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 330, 380]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 0, 50, 100, 150, 200, 250, 300, 350, 400]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080, 1130, 1180, 1230, 1280, 1330, 1380]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 342, 392, 442]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [450, 500, 550, 600, 650, 700, 12, 62, 112, 162, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 354, 404, 454, 504]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [24, 74, 124, 174, 224, 274, 324, 374, 424, 474, 524, 574, 624, 674]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]