tasks = [
    # Generated on 2019-10-14 09:51:16.113000, contains telemetry from sessions 2026 to 2028.
    # The session starts on 2019-10-14 11:11:53+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(46, '/telemetry.current', [884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1884, 1934, 1984, 2034, 2084, 2134, 2184, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1559, 1609, 1659, 1709, 1759, 1809, 1859, 1909, 1959, 2009, 2059, 2109, 2159, 897, 947, 997, 1047, 1097, 1147, 1197]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 921]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 1421, 1471, 1521, 1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1971, 2021, 2071, 2121, 2171, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 915, 965]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615, 1665, 1715, 1765, 1815, 1865, 1915, 1965]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [2015, 2065, 2115, 2165, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 1477, 1527, 1577, 1627, 1677]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [1727, 1777, 1827, 1877, 1927, 1977, 2027, 2077, 2127, 2177, 713]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(40, '/t23n_480_0', [31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t23n_480_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t24n_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t24n_480_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t24n_480_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t24n_480_0', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    # missing from previous session end


    # if good session:    
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]