tasks = [
    # Generated on 2020-01-19 00:05:41.196000, contains telemetry from sessions 2665 to 2666.
    # The session starts on 2020-01-19 09:47:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(61, '/telemetry.previous', [1383, 1433, 1483, 1533, 1583, 1633, 1683, 1733, 1783, 1833, 1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1408, 1458]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [3, 53, 103, 153, 203, 28, 78, 128, 178, 228, 16, 66, 116, 166, 216, 40, 90, 140, 190, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.previous', [1508, 1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1396, 1446, 1496, 1546]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.previous', [1596, 1646, 1696, 1746, 1796, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246, 1420, 1470, 1520, 1570, 1620, 1670]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.previous', [1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1390, 1440, 1490, 1540, 1590, 1640, 1690, 1740]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.previous', [1790, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1402, 1452, 1502, 1552, 1602, 1652, 1702, 1752, 1802, 1852]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [60, 110, 160, 210, 22, 72, 122, 172, 222, 34, 84, 134, 184, 46, 96, 146, 196]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.previous', [1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864, 1914, 1964]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/telemetry.previous', [2014, 2064, 2114, 2164, 2214, 2264, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/telemetry.previous', [2126, 2176, 2226, 2276]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p07n_480_0', [73, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p07w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p07w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p07w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p07w_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p07w_480_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p07w_480_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p07w_480_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p08n_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p08n_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p08n_480_0', [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p08n_480_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p08w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p08w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p08w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p08w_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p08w_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p08w_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p08w_480_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p08w_480_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p09n_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p09n_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p09n_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p09n_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p09n_480_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p09w_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p09w_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p09w_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p09w_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p09w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/p09w_480_0', [112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]