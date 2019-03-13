tasks = [
    # Generated on 2019-03-13 17:56:31.806000, contains telemetry from sessions 643 to 648.
    # The session starts on 2019-03-13 19:51:16+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2046, 2096, 2146, 2196, 2246, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [16, 66, 116, 166, 216, 266, 41, 91, 141, 191, 241, 29, 79, 129, 179, 229, 3, 53, 103, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 83, 133, 183, 233, 283]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [203, 253, 23, 73, 123, 173, 223, 35, 85, 135, 185, 235, 47, 97, 147, 197, 247, 9, 59, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2103, 2153, 2203, 2253, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 89, 139, 189, 239, 289, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189, 1239, 1289, 1339]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [159, 209, 259]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]