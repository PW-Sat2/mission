tasks = [
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

    # Generated on 2019-02-13 19:18:13.192000, contains telemetry from sessions 459 to 466.
    # The session starts on 2019-02-13 20:56:54+01:00.

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1633, 1683, 1733, 1783, 1833, 1883]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1933, 1983, 2033, 2083, 2133, 2183, 2233, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2271, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1615, 1665, 1715, 1765, 1815, 1865]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [2227, 2277, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 1651, 1701, 1751, 1801, 1851]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [2003, 41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1991, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 915]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1965, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1985, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1997, 9, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1959, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1971]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]