tasks = [
    # Generated on 2021-02-06 21:40:09.593453, contains telemetry from sessions 5112 to 5114.
    # The session starts on 2021-02-06 22:02:43+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [2178, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2153, 2203, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [2091, 2141, 2191, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [2065, 2115, 2165, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [2035, 2085, 2135, 2185, 1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1997, 2047, 2097, 2147, 2197, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1959, 2009, 2059, 2109, 2159, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1971, 2021, 2071, 2121, 2171]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missing from previous session start
    [tc.DownloadFile(31, '/p0_n_p480_0', [71, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p0_n_p480_0', [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p0_n_p480_0', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p0_n_p480_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p0_n_p480_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]), Send, WaitMode.Wait],
    # missing from previous session end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
