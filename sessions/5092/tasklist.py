tasks = [
    # Generated on 2021-02-02 23:58:07.094000, contains telemetry from sessions 5091 to 5092.
    # The session starts on 2021-02-03 10:55:30+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446, 1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1946, 1996, 2046, 2096, 2146, 2196, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 2209, 983, 1033, 1083]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1133, 1183, 1233, 1283, 1333, 1383, 1433, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [2133, 2183, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 977, 1027, 1077, 1127, 1177, 1227, 1277]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677, 1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 989, 1039]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1089, 1139, 1189, 1239, 1289, 1339, 1389, 1439, 1489, 1539, 1589, 1639, 1689, 1739, 1789, 1839, 1889, 1939, 1989, 2039]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [2089, 2139, 2189]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start

    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]