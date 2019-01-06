tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
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
    [tc.DownloadFile(30, '/telemetry.previous', [76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1076, 1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2076, 2126, 2176, 2226, 2276, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [46, 96, 146, 196, 246, 296, 346, 396, 446, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [851, 901, 951, 1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1851, 1901, 1951, 2001, 2051, 2101, 2151, 2201, 2251, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189, 1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039, 2089, 2139, 2189, 2239, 113, 163, 213, 263, 313, 363, 413]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [59, 109, 159, 209, 259, 309, 359, 409, 459, 33, 83, 133, 183, 233, 283, 333, 383, 433, 3, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 83, 133, 183]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [2233, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [103, 153, 203, 253, 303, 353, 403, 453, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 27, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2045, 2095, 2145, 2195, 2245, 107, 157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 1607, 1657, 1707, 1757, 1807]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [127, 177, 227, 277, 327, 377, 427, 39, 89, 139, 189, 239, 289, 339, 389, 439]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 1619]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]