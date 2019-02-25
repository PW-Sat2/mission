tasks = [
    # Generated on 2019-02-25 19:35:18.348510, contains telemetry from sessions 537 to 543.
    # The session starts on 2019-02-25 20:17:29+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 1371]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 41, 91, 141, 191, 241, 291, 341, 391]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1359, 1409]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1441, 1491, 1541, 29, 79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 1383, 1433, 1483]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379, 1429, 1479, 1529, 3, 53, 103, 153, 203, 253]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1353, 1403, 1453, 1503, 1553]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1303, 1353, 1403, 1453, 1503, 1553, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 623, 673]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1365, 1415, 1465, 1515, 1565, 1615]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 35, 85, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1377, 1427, 1477, 1527, 1577, 1627, 1677]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]