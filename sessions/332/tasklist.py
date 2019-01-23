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
    [tc.DownloadFile(30, '/telemetry.previous', [1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1477, 1527, 1577]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2022, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1465, 1515, 1565, 1615, 1665, 1715]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1997, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1985, 9, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1939, 1989, 2039, 2089, 2139, 2189, 2239, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1959, 2009, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2109, 2159, 2209, 2259, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1929, 1979, 41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2271, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1495, 1545, 1595]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1941, 1991, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1903, 1953, 2003, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1865, 1915, 1965, 2015]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]