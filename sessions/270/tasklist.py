tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574, 1624]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 699, 749, 799, 849, 899, 949, 999]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1044, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1849, 1899, 1949, 1999]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2049, 2099, 2149, 2199, 2249, 687, 737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [969, 1019, 1069, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 711, 761, 811]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [857, 907, 957, 1007, 1057, 31, 81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [781, 831, 881, 931, 981, 1031, 1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1231, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2231, 693, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [701, 751, 801, 851, 901, 951, 1001, 1051, 13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193, 2243, 705, 755, 805, 855, 905, 955, 1005]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2055, 2105, 2155, 2205, 2255, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 37, 87, 137, 187, 237, 287, 337, 387, 437]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987, 1037]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]