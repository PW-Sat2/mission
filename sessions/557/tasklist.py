tasks = [
    # Generated on 2019-02-27 19:13:35.510691, contains telemetry from sessions 553 to 557.
    # The session starts on 2019-02-27 20:26:11+01:00.

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
    [tc.DownloadFile(30, '/telemetry.current', [1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853, 1903, 1953, 2003]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2053, 2103, 2153, 2203, 2253, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1090, 1140, 1190, 1240, 1290, 1340]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1060, 1110]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [2160, 2210, 2260, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1922, 1972, 2022, 2072, 2122, 2172, 2222, 2272, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 1446]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1496, 1546, 1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]