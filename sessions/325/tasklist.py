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
    [tc.DownloadFile(30, '/telemetry.previous', [1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2090, 2140, 2190, 2240, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 35, 85, 135, 185, 235, 285]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1335, 1385, 1435, 1485, 1535, 1585, 1635, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [673, 723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1097, 1147, 1197, 1247]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 17, 67, 117, 167, 217, 267, 317]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [367, 417, 467, 517, 567, 617, 667, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1367, 1417, 1467, 1517, 1567, 1617, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2109, 2159, 2209, 2259, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 41]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 3, 53, 103, 153, 203, 253, 303, 353]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1403, 1453, 1503, 1553, 1603, 1653]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]