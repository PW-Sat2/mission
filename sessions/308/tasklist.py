tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 587, 637, 687, 737, 787, 837, 887, 937, 987, 1037]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1557, 1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481, 1531]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]