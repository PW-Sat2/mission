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
    [tc.DownloadFile(30, '/telemetry.previous', [1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 21, 71, 121, 171, 221, 271]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 1339]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 9, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1363, 1413]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1559, 1609, 1659, 1709, 33, 83, 133, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 1333, 1383, 1433]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683, 3, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1345, 1395, 1445, 1495]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 15, 65, 115, 165, 215, 265, 315]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1357, 1407, 1457, 1507, 1557]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 1369, 1419, 1469, 1519, 1569, 1619]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1627, 1677, 39, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [939, 989, 1039, 1089, 1139, 1189, 1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 1639, 1689]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]