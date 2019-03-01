tasks = [
    # Generated on 2019-03-01 23:24:01.212000, contains telemetry from sessions 571 to 572.
    # The session starts on 2019-03-02 09:45:09+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # 8th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_8'), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [849, 899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1849, 1899, 1949, 1999, 2049, 2099, 2149, 874, 924, 974, 1024, 1074, 1124, 1174, 1224, 1274, 1324, 1374, 1424, 1474]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 862, 912, 962, 1012, 1062, 1112, 1162]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [886, 936, 986, 1036, 1086, 1136, 1186, 1236, 1286, 1336, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736, 1786, 1836]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1886, 1936, 1986, 2036, 2086, 2136, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 868, 918, 968, 1018, 1068, 1118, 1168]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1218, 1268, 1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 880]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [930, 980, 1030, 1080, 1130, 1180, 1230, 1280, 1330, 1380, 1430, 1480, 1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1930, 1980, 2030, 2080, 2130, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 1392, 1442, 1492, 1542, 1592]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]