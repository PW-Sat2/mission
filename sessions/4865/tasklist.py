tasks = [
    # Generated on 2020-12-26 23:42:33.610000, contains telemetry from sessions 4864 to 4865.
    # The session starts on 2020-12-27 10:45:04+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [[tc.SetBitrate(4, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(60, '/telemetry.previous', [1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1372]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [17, 67, 117, 167, 217, 267, 317, 42, 92, 142, 192, 242, 292, 342, 30, 80, 130, 180, 230, 280]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [1422, 1472, 1522, 1572, 1622, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172, 2222, 2272, 1360, 1410]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1384, 1434, 1484]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [330, 4, 54, 104, 154, 204, 254, 304, 24, 74, 124, 174, 224, 274, 324, 36, 86, 136, 186, 236]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.previous', [1534, 1584, 1634, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1354, 1404, 1454, 1504, 1554]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.previous', [1604, 1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1366, 1416, 1466, 1516, 1566, 1616]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.previous', [1666, 1716, 1766, 1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1378, 1428, 1478, 1528, 1578, 1628, 1678]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [286, 336, 48, 98, 148, 198, 248, 298, 348, 10, 60, 110, 160, 210, 260, 310]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.previous', [1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.previous', [1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/a_w_p480_11_32_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a_w_p480_11_32_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_w_p480_11_32_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_w_p480_11_32_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_p480_11_32_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_p480_11_32_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_p480_11_40_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_p480_11_40_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_p480_11_40_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_p480_11_40_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_p480_11_52_0', [7, 8, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_p480_11_52_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_p480_11_52_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_w_p480_11_52_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_p480_11_56_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_w_p480_11_56_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_p480_11_56_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_p480_11_56_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_p480_12_00_0', [10, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_p480_12_00_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_p480_12_00_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_p480_12_00_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_p480_12_04_0', [10, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_w_p480_12_04_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_p480_12_04_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_w_p480_12_04_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a_w_p480_12_04_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a_w_p480_12_04_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]