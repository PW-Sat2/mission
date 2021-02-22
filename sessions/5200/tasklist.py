tasks = [
    # Generated on 2021-02-22 11:19:28.888323, contains telemetry from sessions 5199 to 5200.
    # The session starts on 2021-02-22 12:32:13+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(60, '/telemetry.current', [729, 779, 829, 879, 929, 754, 804, 854, 904, 742, 792, 842, 892, 766, 816, 866, 916, 736, 786, 836]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [886, 748, 798, 848, 898, 760, 810, 860, 910, 772, 822, 872, 922]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(36, '/telemetry.previous', [698, 704, 710, 722, 728, 734, 748, 754, 760, 772, 778, 784, 798, 804, 810, 822, 828, 834, 848, 854]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [860, 872, 878, 884, 898, 904, 910, 922, 928, 934, 948, 954, 960, 972, 978, 984, 998, 1004, 1010, 1022]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1028, 1034, 1048, 1054, 1060, 1072, 1078, 1084, 1098, 1104, 1110, 1116, 1122, 1128, 1134, 1148, 1154, 1160, 1166, 1172]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1178, 1184, 1198, 1204, 1210, 1216, 1222, 1228, 1234, 1248, 1254, 1260, 1266, 1272, 1278, 1284, 1298, 1304, 1310, 1316]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1322, 1328, 1334, 1348, 1354, 1360, 1366, 1372, 1378, 1384, 1398, 1404, 1410, 1416, 1422, 1428, 1434, 1448, 1454, 1460]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1466, 1472, 1478, 1484, 1498, 1504, 1510, 1516, 1522, 1528, 1534, 1548, 1554, 1560, 1566, 1572, 1578, 1584, 1598, 1604]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1610, 1616, 1622, 1628, 1634, 1641, 1648, 1654, 1660, 1666, 1672, 1678, 1684, 1698, 1704, 1710, 1716, 1722, 1728, 1734]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1748, 1754, 1760, 1766, 1772, 1778, 1784, 1798, 1804, 1810, 1816, 1822, 1828, 1834, 1848, 1854, 1860, 1866, 1872, 1878]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1884, 1898, 1904, 1910, 1916, 1922, 1928, 1934, 1948, 1954, 1960, 1966, 1972, 1978, 1984, 1998, 2004, 2010, 2016]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [2022, 2028, 2034, 2048, 2054, 2060, 2066, 2072, 2078, 2084, 2098, 2104, 2110, 2116, 2122, 2128, 2134, 2148, 2154]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2160, 2166, 2172, 2178, 2184, 2198, 2204, 2210, 2216, 2222, 2228, 2234, 2241, 2248, 2254, 2260, 2266, 2272, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/telemetry.current', [4, 18, 24, 30, 42, 48, 54, 68, 74, 80, 86, 92, 98, 104, 118, 124, 130, 136, 142]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [148, 154, 168, 174, 180, 192, 198, 204, 218, 224, 230, 236, 242, 248, 254, 268, 274, 280, 286]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [292, 298, 304, 311, 318, 324, 330, 336, 342, 348, 354, 361, 368, 374, 380, 386, 392, 398, 404]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [411, 418, 424, 430, 436, 442, 448, 454, 468, 474, 480, 486, 492, 498, 504, 518, 524, 530]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [536, 542, 548, 554, 568, 574, 580, 586, 592, 598, 604, 611, 618, 624, 630, 636, 642, 648]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [654, 661, 668, 674, 680, 686, 692, 698, 704, 718, 724, 730, 736, 742, 748, 754, 768, 774]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/pw_p10_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/pw_p10_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/pw_p10_0', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
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