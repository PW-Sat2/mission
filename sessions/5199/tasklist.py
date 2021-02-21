tasks = [
    # Generated on 2021-02-21 22:57:37.764000, contains telemetry from sessions 5195 to 5199.
    # The session starts on 2021-02-22 11:07:23+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 716, 766, 816, 866, 916, 966, 1016, 1066]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [11, 61, 111, 161, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 36, 86, 136, 186]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 1616, 1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2116, 2166, 2216, 2266, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [236, 286, 336, 386, 436, 486, 536, 586, 636, 686, 736, 24, 74, 124, 174, 224, 274, 324, 374, 424]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1504, 1554, 1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 728, 778, 828, 878]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [474, 524, 574, 624, 674, 724, 774, 48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 1578, 1628, 1678, 1728, 1778, 1828, 1878]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [698, 748, 18, 68, 118, 168, 218, 268, 318, 368, 418, 468, 518, 568, 618, 668, 718, 768, 30, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 1460, 1510, 1560, 1610, 1660]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 722, 772, 822, 872, 922, 972, 1022, 1072]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [130, 180, 230, 280, 330, 380, 430, 480, 530, 580, 630, 680, 730, 42, 92, 142, 192, 242, 292, 342]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1122, 1172, 1222, 1272, 1322, 1372, 1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2122, 2172, 2222, 2272, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 1484]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [392, 442, 492, 542, 592, 642, 692, 742, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [604, 654, 704, 754]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(58, '/pw_p10_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/pw_p10_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/pw_p10_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(77, 'n01n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(78, 'n01w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(79, 'n02n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(80, 'n02w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(81, 'p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(82, 'p1_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(83, 'p1_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(84, 'p1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(85, 'p2_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(86, 'p2_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(87, 'p5174_0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(88, 'p5174_1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(89, 'radfet_60'), Send, WaitMode.Wait],
    [tc.RemoveFile(90, 'radfet_61'), Send, WaitMode.Wait],
    [tc.ListFiles(91, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]