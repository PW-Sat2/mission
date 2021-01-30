tasks = [
    # Generated on 2021-01-30 17:53:53.203847, contains telemetry from sessions 5065 to 5071.
    # The session starts on 2021-01-30 21:27:46+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1001, 1051, 1101, 1151, 1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 1601, 1651, 1701, 1751, 1801, 1851, 1901, 1951]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [2001, 2051, 2101, 2151, 2201, 2251, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 46, 96, 146, 196, 246, 296, 346, 396, 446, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176, 1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176, 2226, 2276, 14, 64, 114, 164, 214, 264, 314, 364]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 38, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [84, 134, 184, 234, 284, 334, 384, 434, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 28, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1138, 1188, 1238, 1288, 1338, 1388, 1438, 1488, 1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [2138, 2188, 2238, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [858, 908, 958, 1008, 1058, 1108, 1158, 1208, 1258, 1308, 1358, 1408, 1458, 1508, 1558, 1608, 1658, 1708, 1758, 1808]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [128, 178, 228, 278, 328, 378, 428, 40, 90, 140, 190, 240, 290, 340, 390, 440, 2, 52, 102, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470, 1520]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 32, 82, 132, 182, 232]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [202, 252, 302, 352, 402, 452, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [44, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [2044, 2094, 2144, 2194, 2244]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]