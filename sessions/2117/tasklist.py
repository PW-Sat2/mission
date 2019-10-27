tasks = [
    # Generated on 2019-10-27 18:40:54.374000, contains telemetry from sessions 2116 to 2117.
    # The session starts on 2019-10-27 19:10:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(76, '/telemetry.previous', [1803, 1853, 1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [23, 73, 123, 173, 223, 48, 98, 148, 198, 36, 86, 136, 186, 236, 10, 60, 110, 160, 210, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/telemetry.previous', [1816, 1866, 1916, 1966, 2016, 2066, 2116, 2166, 2216, 2266, 1840, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240, 1810]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/telemetry.previous', [1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1822, 1872, 1922, 1972, 2022, 2072, 2122, 2172, 2222, 2272, 1834]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/telemetry.current', [80, 130, 180, 230, 42, 92, 142, 192, 242, 4, 54, 104, 154, 204, 16, 66, 116, 166, 216]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/telemetry.previous', [1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1846, 1896, 1946, 1996, 2046, 2096, 2146, 2196, 2246]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [582, 882, 1623, 1630, 1636, 1642, 1648, 1654, 1660, 1666, 1673, 1680, 1686, 1692, 1698, 1704, 1710, 1716, 1723]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1730, 1736, 1742, 1748, 1754, 1760, 1766, 1773, 1780, 1786, 1792, 1798, 1804, 1810, 1816, 1823, 1830, 1836, 1842]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t02w_240_10', [1, 3, 4, 6, 7, 10, 11, 12, 15, 16, 42, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t02w_240_14', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02w_240_20', [9, 10, 14, 15, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t02w_240_23', [5, 7, 30]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t02w_240_24', [0, 32, 33, 34, 35, 43, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t02w_240_21', [0, 16, 17, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t02w_240_21', [53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t02w_240_22', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t02w_240_22', [10, 11, 12, 13, 14, 15, 16, 23, 24, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t02w_240_25', [14, 16, 20, 36, 37, 38, 39, 40, 41, 42, 43]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t02w_240_25', [44, 45, 46, 47, 48, 49, 50, 51, 52, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t02w_240_26', [5, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t02w_240_26', [38, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 74]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t02w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t02w_240_3', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t02w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t02w_240_4', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t02w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t02w_240_5', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t02w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t02w_240_6', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t02w_240_16', [5, 8, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t02w_240_16', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t02w_240_16', [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t02w_240_17', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t02w_240_17', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t02w_240_17', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t02w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t02w_240_7', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t02w_240_7', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t02w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t02w_240_8', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t02w_240_8', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t02w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t02w_240_9', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t02w_240_9', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t02w_240_27', [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t02w_240_27', [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t02w_240_27', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t02w_240_27', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t02w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t02w_240_28', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t02w_240_28', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t02w_240_28', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]