tasks = [
    # Generated on 2019-02-17 11:02:08.482000, contains telemetry from sessions 489 to 490 and missings since 486.
    # The session starts on 2019-02-17 11:57:26+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2205, 2255, 2230, 2218, 2268, 2242, 2212, 2262, 2224, 2274, 2236, 2248]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [25, 75, 125, 0, 50, 100, 38, 88, 138, 12, 62, 112, 32, 82, 132, 44, 94, 144, 6, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [106, 18, 68, 118]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missings since 486
    [tc.DownloadFile(40, '/telemetry.previous', [768, 842, 918, 992, 1068, 1142, 1218, 1292, 1368, 1442, 1518, 1592, 1668, 1742, 1818, 1892, 1968, 2042, 2118, 2192]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [774, 848, 924, 998, 1074, 1148, 1224, 1298, 1374, 1448, 1524, 1598, 1674, 1748, 1824, 1898, 1974, 2048, 2124, 2198]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [780, 854, 930, 1004, 1080, 1154, 1230, 1304, 1380, 1454, 1530, 1604, 1680, 1754, 1830, 1904, 1980, 2054, 2130, 2204]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [792, 868, 942, 1018, 1092, 1168, 1242, 1318, 1392, 1468, 1542, 1618, 1692, 1768, 1842, 1918, 1992, 2068, 2142, 2218]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [798, 874, 948, 1024, 1098, 1174, 1248, 1324, 1398, 1474, 1548, 1624, 1698, 1774, 1848, 1924, 1998, 2074, 2148, 2224]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [804, 880, 954, 1030, 1104, 1180, 1254, 1330, 1404, 1480, 1554, 1630, 1704, 1780, 1854, 1930, 2004, 2080, 2154, 2230]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [818, 892, 968, 1042, 1118, 1192, 1268, 1342, 1418, 1492, 1568, 1642, 1718, 1792, 1868, 1942, 2018, 2092, 2168, 2242]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [824, 898, 974, 1048, 1124, 1198, 1274, 1348, 1424, 1498, 1574, 1648, 1724, 1798, 1874, 1948, 2024, 2098, 2174, 2248]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [830, 904, 980, 1054, 1130, 1204, 1280, 1354, 1430, 1504, 1580, 1654, 1730, 1804, 1880, 1954, 2030, 2104, 2180]), Send, WaitMode.Wait],

    # Low res photos download
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]