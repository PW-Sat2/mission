tasks = [
    # Generated on 2019-02-19 17:35:23.192000, contains telemetry from sessions 498 to 503.
    # The session starts on 2019-02-19 19:50:56+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1511, 1561, 1611, 1661]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1006, 1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 31, 81, 131, 181, 231]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1569, 1619, 1669, 43, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2123, 2173, 2223, 2273, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 13, 63, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 25, 75, 125, 175, 225, 275, 325, 375]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1517, 1567, 1617, 1667]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1425, 1475, 1525, 1575, 1625, 1675, 37, 87, 137, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [49, 99, 149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]