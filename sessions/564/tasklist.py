tasks = [
    # Generated on 2019-02-28 13:42:33.920000, contains telemetry from sessions 558 to 564.
    # The session starts on 2019-02-28 20:30:31+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2134, 2184, 2234, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [4, 54, 104, 154, 204, 254, 304, 354, 29, 79, 129, 179, 229, 279, 329, 17, 67, 117, 167, 217]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2009, 2059, 2109, 2159, 2209, 2259, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [267, 317, 41, 91, 141, 191, 241, 291, 341, 11, 61, 111, 161, 211, 261, 311, 23, 73, 123, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 141, 191, 241, 291, 341, 391, 441, 491]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 153, 203, 253, 303, 353]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 165, 215]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [223, 273, 323, 35, 85, 135, 185, 235, 285, 335, 47, 97, 147, 197, 247, 297, 347]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2265, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [2127, 2177, 2227, 2277]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]