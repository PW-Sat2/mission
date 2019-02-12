tasks = [
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
    [tc.DownloadFile(30, '/telemetry.previous', [1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1443, 1493]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888, 938, 988]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 1488, 1538, 1588, 1638, 13, 63, 113, 163, 213, 263, 313]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 1431, 1481, 1531, 1581, 1631]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1363, 1413, 1463, 1513, 1563, 1613, 1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 45, 95, 145, 195, 245, 295, 345, 395]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1975, 2025, 2075, 2125, 2175, 2225, 2275, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1445, 1495, 1545, 1595, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [2087, 2137, 2187, 2237, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 19, 69, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2249, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 31, 81, 131, 181, 231, 281, 331, 381, 431, 481]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1531, 1581, 1631]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]