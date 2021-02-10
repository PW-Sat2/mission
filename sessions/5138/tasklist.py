tasks = [
    # Generated on 2021-02-10 23:27:33.694734, contains telemetry from sessions 5136 to 5138.
    # The session starts on 2021-02-11 10:19:16+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1420, 1470]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [15, 65, 115, 165, 215, 265, 315, 365, 40, 90, 140, 190, 240, 290, 340, 28, 78, 128, 178, 228]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1520, 1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1408, 1458, 1508, 1558]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1432, 1482, 1532, 1582, 1632, 1682]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [278, 328, 378, 2, 52, 102, 152, 202, 252, 302, 352, 22, 72, 122, 172, 222, 272, 322, 372, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1964, 2014, 2064, 2114, 2164, 2214, 2264, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [84, 134, 184, 234, 284, 334, 46, 96, 146, 196, 246, 296, 346, 8, 58, 108, 158, 208, 258, 308]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2076, 2126, 2176, 2226, 2276, 1438, 1488, 1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2188, 2238]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [358]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]