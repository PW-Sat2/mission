tasks = [
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
    [tc.DownloadFile(30, '/telemetry.previous', [478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 503, 553, 603]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 23, 73, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 491, 541, 591, 641, 691, 741, 791]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723, 773, 823, 873, 11, 61, 111, 161, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 515, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 35, 85, 135, 185, 235, 285, 335]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2065, 2115, 2165, 2215, 2265, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 5, 55, 105, 155, 205, 255, 305, 355, 405, 455]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2235, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [505, 555, 605, 655, 705, 755, 805, 855, 17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 509, 559, 609]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [617, 667, 717, 767, 817, 867, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 521, 571, 621, 671, 721, 771, 821]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [729, 779, 829, 41, 91, 141, 191, 241, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741, 791, 841]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]