tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2000, 2050, 2100, 2150, 2200, 2250, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575, 625, 675]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [20, 70, 45, 95, 33, 83, 7, 57, 107, 27, 77, 39, 89, 1, 51, 101, 13, 63, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 1625, 1675]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 13, 63, 113, 163, 213, 263, 313, 363]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 37, 87]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [137, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987, 1037, 1087]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2137, 2187, 2237, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1569, 1619, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 31, 81, 131, 181, 231]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [43, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [2043, 2093, 2143, 2193, 2243]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]