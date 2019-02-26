tasks = [
    # Generated on 2019-02-26 12:52:45.884000, contains telemetry from sessions 543 to 550.
    # The session starts on 2019-02-26 20:21:50+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1555, 1605, 1655, 1705, 1755]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 25]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 13, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [2043, 2093, 2143, 2193, 2243, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 37, 87, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987, 1037, 1087, 1137]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 7, 57, 107, 157, 207]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1549, 1599, 1649, 1699, 1749]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 19, 69, 119, 169, 219, 269]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 31, 81, 131, 181, 231, 281, 331]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [2061, 2111, 2161, 2211, 2261, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 43, 93, 143, 193, 243, 293, 343, 393, 443]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    # remove files
    [tc.RemoveFile(100, 'p1_480_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(101, 'p4_480_0' ), Send, WaitMode.Wait],
    [tc.RemoveFile(102, 'p7_480_0' ), Send, WaitMode.Wait],
    
    [tc.ListFiles(112, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
