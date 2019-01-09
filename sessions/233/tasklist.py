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
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [12, 62, 112, 162, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1012, 1062, 1112, 1162, 37, 87, 137, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [837, 887, 937, 987, 1037, 1087, 1137, 1187, 25, 75, 125, 175, 225, 275, 325, 375, 425, 475, 525, 575]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 49, 99, 149, 199, 249, 299, 349, 399]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 19, 69, 119, 169, 219]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211, 1261]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [81, 131, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1081, 1131, 1181, 43, 93, 143, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [893, 943, 993, 1043, 1093, 1143, 5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [705, 755, 805, 855, 905, 955, 1005, 1055, 1105, 1155]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(60, '/p3_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p3_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(62, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p4_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(64, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p5_128_0', [i for i in range(18, 35, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]