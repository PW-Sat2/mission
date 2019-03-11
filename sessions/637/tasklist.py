tasks = [
    # Generated on 2019-03-11 17:45:42.253000, contains telemetry from sessions 631 to 637.
    # The session starts on 2019-03-11 21:16:47+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172, 2222, 2272, 1647, 1697, 1747, 1797, 1847, 1897]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1947, 1997, 2047, 2097, 2147, 2197, 2247, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 1629, 1679, 1729, 1779, 1829, 1879, 1929]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1979, 2029, 2079, 2129, 2179, 2229, 2279, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1665, 1715, 1765, 1815, 1865, 1915, 1965]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [2015, 2065, 2115, 2165, 2215, 2265]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [42, 92, 142, 192, 242, 292, 342, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 617, 667, 717, 767, 817, 867, 917, 967]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [2017, 5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855, 1905]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1955, 2005, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1929, 1979, 49, 99, 149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1949, 1999, 11, 61, 111, 161, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [911, 961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1911, 1961, 2011, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773, 823]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1873, 1923, 1973, 35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1885, 1935, 1985]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]