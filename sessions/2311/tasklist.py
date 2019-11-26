tasks = [
    # Generated on 2019-11-26 09:23:26.305590, contains telemetry from sessions 2308 to 2311.
    # The session starts on 2019-11-26 10:10:26+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395, 1445, 1495, 1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2045, 2095, 2145, 2195, 2245, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [15, 65, 115, 165, 215, 40, 90, 140, 190, 240, 28, 78, 128, 178, 228, 2, 52, 102, 152, 202]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1082, 1132, 1182, 1232, 1282]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1052]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1102, 1152, 1202, 1252, 1302, 1352, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2102, 2152, 2202, 2252, 1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [22, 72, 122, 172, 222, 34, 84, 134, 184, 234, 46, 96, 146, 196, 8, 58, 108, 158, 208]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1076, 1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 1088, 1138, 1188, 1238, 1288, 1338]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1388, 1438, 1488, 1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [11, 61, 111, 161, 211, 36, 86, 136, 186, 236, 24, 74, 124, 174, 224, 48, 98, 148, 198, 248]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [18, 68, 118, 168, 218, 30, 80, 130, 180, 230, 42, 92, 142, 192, 242, 4, 54, 104, 154, 204]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [254]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]