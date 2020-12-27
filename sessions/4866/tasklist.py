tasks = [
    # Generated on 2020-12-27 10:59:23.109816, contains telemetry from sessions 4865 to 4866.
    # The session starts on 2020-12-27 12:17:51+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(70, '/telemetry.current', [320, 370, 420, 470, 520, 345, 395, 445, 495, 333, 383, 433, 483, 533, 357, 407, 457, 507, 327, 377]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [427, 477, 527, 339, 389, 439, 489, 351, 401, 451, 501, 363, 413, 463, 513]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [4, 10, 17, 24, 30, 36, 42, 48, 54, 60, 67, 74, 80, 86, 92, 98, 104, 110, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [124, 130, 136, 142, 148, 154, 160, 167, 174, 180, 186, 192, 198, 204, 210, 217, 224, 230, 236]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [242, 248, 254, 260, 267, 274, 280, 286, 292, 298, 304, 310, 317, 324, 330, 336, 342, 348]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1354, 1360, 1366, 1378, 1384, 1390, 1404, 1410, 1416, 1422, 1428, 1434, 1440, 1454, 1460, 1466, 1472, 1478, 1484]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1490, 1504, 1510, 1516, 1522, 1528, 1534, 1540, 1554, 1560, 1566, 1572, 1578, 1584, 1590, 1604, 1610, 1616, 1622]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1628, 1634, 1640, 1654, 1660, 1666, 1672, 1678, 1684, 1690, 1704, 1710, 1716, 1722, 1728, 1734, 1740, 1754, 1760]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1766, 1772, 1778, 1784, 1790, 1804, 1810, 1816, 1822, 1828, 1834, 1840, 1854, 1860, 1866, 1872, 1878, 1884, 1890]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1904, 1910, 1916, 1922, 1928, 1934, 1940, 1954, 1960, 1966, 1972, 1978, 1984, 1990, 2004, 2010, 2016, 2022]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2028, 2034, 2040, 2054, 2060, 2066, 2072, 2078, 2084, 2090, 2104, 2110, 2116, 2122, 2128, 2134, 2140, 2154]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2160, 2166, 2172, 2178, 2184, 2190, 2204, 2210, 2216, 2222, 2228, 2234, 2240, 2254, 2260, 2266, 2272, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_p480_11_32_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_p480_11_32_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_p480_11_32_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_w_p480_11_32_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_p480_11_32_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_w_p480_11_32_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_p480_11_40_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_p480_11_40_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_p480_11_40_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_p480_11_40_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_p480_11_52_0', [7, 8, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_p480_11_52_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_p480_11_52_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_w_p480_11_52_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_p480_11_56_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_w_p480_11_56_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a_w_p480_11_56_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a_w_p480_11_56_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a_w_p480_12_00_0', [10, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_p480_12_00_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a_w_p480_12_00_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_w_p480_12_00_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a_w_p480_12_04_0', [10, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a_w_p480_12_04_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a_w_p480_12_04_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a_w_p480_12_04_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a_w_p480_12_04_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a_w_p480_12_04_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]