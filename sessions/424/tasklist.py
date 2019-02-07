tasks = [
    # Generated on 2019-02-07 01:12:39.974572, contains telemetry from sessions 417 to 424.
    # The session starts on 2019-02-07 20:28:51+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2010, 2060, 2110, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2215, 2265, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1777, 1827, 1877, 1927, 1977, 2027, 2077]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1885, 1935, 1985, 2035, 2085, 2135, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2127, 2177, 2227, 2277, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1759, 1809, 1859, 1909, 1959]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 17, 67, 117, 167, 217, 267, 317, 367, 417]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [467, 517, 567, 617, 667, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 29, 79, 129, 179, 229, 279]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [2009, 2059, 2109, 2159, 2209, 2259, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1783, 1833, 1883]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 41, 91, 141]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 3]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1933, 1983, 2033, 2083, 2133, 2183, 2233]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [2053, 2103]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]