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
    [tc.DownloadFile(30, '/telemetry.previous', [972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1972, 2022, 2072, 2122, 2172, 2222, 2272, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [42, 92, 142, 192, 242, 292, 342, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1042, 1092, 1142, 1192, 1242, 1292, 1342, 17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 617]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 985, 1035, 1085, 1135, 1185, 1235, 1285]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [667, 717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 5, 55, 105, 155, 205]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235, 1009]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1255, 1305, 1355, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2059, 2109, 2159, 2209, 2259, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 49, 99, 149, 199, 249, 299, 349, 399, 449, 499]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 11, 61, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 1003, 1053]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [161, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061, 1111]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1161, 1211, 1261, 1311, 1361, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2103, 2153, 2203, 2253, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 35, 85, 135, 185, 235, 285, 335, 385]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]