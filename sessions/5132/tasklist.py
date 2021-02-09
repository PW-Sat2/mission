tasks = [
    # Generated on 2021-02-10 00:17:17.541000, contains telemetry from sessions 5131 to 5132.
    # The session starts on 2021-02-10 11:09:53+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2141, 2191, 2241, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [11, 61, 111, 36, 86, 24, 74, 48, 98, 18, 68, 118, 30, 80, 42, 92, 4, 54, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [2016, 2066, 2116, 2166, 2216, 2266, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 1604, 1654, 1704, 1754, 1804]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248, 1160, 1210, 1260, 1310, 1360]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1172, 1222]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172, 2222]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2272, 1184, 1234, 1284, 1334, 1384, 1434, 1484, 1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2134, 2184, 2234]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(41, '/n01n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(42, '/n01w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(43, '/n02n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(44, '/n02w_0'), Send, WaitMode.Wait],
    [tc.ListFiles(45, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]