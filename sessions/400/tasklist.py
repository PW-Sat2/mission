tasks = [
    # Generated on 2019-02-04 09:59:49.613000, contains telemetry from sessions 397 to 400

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [11, 36, 24, 48, 18, 30, 42, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 854, 904]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1954, 2004, 2054, 2104, 2154, 2204, 2254, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 848, 898, 948, 998]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1048, 1098, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2048, 2098, 2148, 2198, 2248, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 872, 922, 972, 1022, 1072, 1122]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [2172, 2222, 2272, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]