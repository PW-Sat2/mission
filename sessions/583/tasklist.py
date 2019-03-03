tasks = [
    # Generated on 2019-03-03 14:17:26.748000, contains telemetry from sessions 576 to 583.
    # The session starts on 2019-03-03 20:43:23+01:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393, 1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 1893, 1943, 1993]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2043, 2093, 2143, 2193, 2243, 1068, 1118, 1168, 1218, 1268, 1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 2218, 2268, 1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 26, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 1080, 1130, 1180, 1230, 1280]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1126, 1176, 1226, 1276, 1326, 1376, 1426, 0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1050]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 20, 70, 120, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [2100, 2150, 2200, 2250, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1220, 1270, 1320, 1370, 1420, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 44, 94, 144, 194, 244, 294]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 1086, 1136, 1186, 1236, 1286, 1336]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1344, 1394, 6, 56, 106, 156, 206, 256, 306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]