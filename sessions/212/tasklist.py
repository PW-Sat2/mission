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
    [tc.DownloadFile(30, '/telemetry.previous', [1993, 2043, 2093, 2143, 2193, 2243, 2018, 2068, 2118, 2168, 2218, 2268, 2006, 2056, 2106, 2156, 2206, 2256, 2030, 2080]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 1613, 1663, 1713, 1763, 1813, 1863, 1913, 1963]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2013, 2063, 2113, 2163, 2213, 2263, 2313, 2363, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 1488, 1538, 1588]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 2288, 2338, 2388, 26, 76, 126, 176]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [2226, 2276, 2326, 2376, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2130, 2180, 2230, 2000, 2050, 2100, 2150, 2200, 2250, 2012, 2062, 2112, 2162, 2212, 2262, 2024, 2074, 2124, 2174, 2224]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 2300, 2350, 20, 70, 120, 170, 220, 270, 320, 370]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 2320, 2370]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [2032, 2082, 2132, 2182, 2232, 2282, 2332, 2382, 44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [2274, 2036, 2086, 2136, 2186, 2236]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 2294, 2344, 6, 56, 106, 156, 206]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156, 1206]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [2256, 2306, 2356]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]