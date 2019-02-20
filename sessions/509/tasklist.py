tasks = [
    # Generated on 2019-02-20 19:41:04.922107, contains telemetry from sessions 503 to 509.
    # The session starts on 2019-02-20 19:55:23+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1691, 1741, 1791, 1841, 1891, 1941, 1991]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2041, 2091, 2141, 2191, 2241, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1703, 1753]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [2173, 2223, 2273, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235, 1697, 1747, 1797, 1847, 1897]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1947, 1997, 2047, 2097, 2147, 2197, 2247, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [36, 86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686, 736, 786, 836, 886, 936, 986]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1036, 1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2036, 11, 61, 111, 161, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1961, 2011, 2061, 49, 99, 149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1899, 1949, 1999, 2049, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1823, 1873, 1923, 1973, 2023, 43, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1793, 1843, 1893, 1943, 1993, 2043, 5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [705, 755, 805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1705, 1755, 1805, 1855, 1905, 1955, 2005, 2055, 17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [617, 667, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
