tasks = [
    # Generated on 2019-03-07 18:02:54.555000, contains telemetry from sessions 604 to 611.
    # The session starts on 2019-03-07 21:00:26+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1190, 1240, 1290, 1340, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2190, 2240, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 35, 85, 135, 185, 235, 285, 335, 385]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2115, 2165, 2215, 2265, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [435, 485, 535, 585, 23, 73, 123, 173, 223, 273, 323, 373, 423, 473, 523, 573, 47, 97, 147, 197]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2003, 2053, 2103, 2153, 2203, 2253, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1927, 1977, 2027, 2077, 2127, 2177, 2227, 2277, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [247, 297, 347, 397, 447, 497, 547, 17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 2259, 221, 271, 321, 371, 421, 471, 521, 571]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [79, 129, 179, 229, 279, 329, 379, 429, 479, 529, 579, 41, 91, 141, 191, 241, 291, 341, 391, 441]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 233, 283, 333, 383, 433, 483]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [491, 541, 3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]