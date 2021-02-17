tasks = [
    # Generated on 2021-02-17 13:59:27.027033, contains telemetry from sessions 5173 to 5174.
    # The session starts on 2021-02-17 21:09:23+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.previous', [1571, 1621, 1671, 1721, 1771, 1821, 1871, 1921, 1971, 2021, 2071, 2121, 2171, 2221, 2271, 1596, 1646, 1696, 1746, 1796]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [41, 91, 141, 16, 66, 116, 4, 54, 104, 28, 78, 128, 48, 98, 10, 60, 110, 22, 72, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2134, 2184, 2234, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1578, 1628, 1678]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1590, 1640, 1690, 1740, 1790, 1840, 1890, 1940]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1990, 2040, 2090, 2140, 2190, 2240, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [34, 84, 134]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(33, '/p1_w_p480_0', [22, 53, 54, 58, 59]), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.previous', [78, 84, 240, 360, 703, 716, 928, 990, 1134, 1140, 1146, 1178, 1184, 1190, 1196]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1237, 1261, 1402, 1408, 1414, 1420, 1426, 1432, 1438, 1452, 1458, 1464, 1476, 1482]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1488, 1495, 1502, 1508, 1514, 1526, 1532, 1538, 1552, 1564, 1576, 1582, 1588, 1602]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]