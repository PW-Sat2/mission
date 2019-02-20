tasks = [
    # Generated on 2019-02-20 20:09:49.695825, contains telemetry from sessions 503 to 510.
    # The session starts on 2019-02-20 21:29:16+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
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
    [tc.DownloadFile(30, '/telemetry.current', [2024, 2074, 2124, 2174, 2224, 2049, 2099, 2149, 2199, 2037, 2087, 2137, 2187, 2237, 2061, 2111, 2161, 2211, 2031, 2081]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2131, 2181, 2231, 2043, 2093, 2143, 2193, 2243, 2055, 2105, 2155, 2205, 2067, 2117, 2167, 2217]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]