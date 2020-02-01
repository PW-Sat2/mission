tasks = [
    # Generated on 2020-02-01 20:51:17.057000, contains telemetry from sessions 2752 to 2755.
    # The session starts on 2020-02-01 21:07:34+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.previous', [1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 1650, 1700, 1750, 1800, 1850, 1900]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [45, 95, 145, 195, 245, 295, 345, 395, 20, 70, 120, 170, 220, 270, 320, 370, 8, 58, 108, 158]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1950, 2000, 2050, 2100, 2150, 2200, 2250, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [208, 258, 308, 358, 32, 82, 132, 182, 232, 282, 332, 382, 2, 52, 102, 152, 202, 252, 302, 352]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1632, 1682, 1732, 1782, 1832, 1882, 1932]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1982, 2032, 2082, 2132, 2182, 2232, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1656]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [402, 14, 64, 114, 164, 214, 264, 314, 364, 26, 76, 126, 176, 226, 276, 326, 376, 38, 88, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1706, 1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 2206, 2256, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2068, 2118, 2168, 2218, 2268]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [188, 238, 288, 338, 388]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(130, '/t03w_240_20', [8]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/t03w_240_23', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/t03w_240_24', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/t03w_240_25', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/t03w_240_26', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/t03w_240_27', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/t03w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/t03w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/t03w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/t03w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(140, '/t03w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/t03w_240_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/t03w_240_8', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/t03w_240_9', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(144, '/t04w_240_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/t04w_240_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(146, '/t04w_240_1', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(147, '/t04w_240_1', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(148, '/t04w_240_2', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(149, '/t04w_240_2', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(150, '/t04w_240_3', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/t04w_240_3', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/t04w_240_6', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/t04w_240_6', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/t04w_240_6', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/t04w_240_4', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(156, '/t04w_240_4', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(157, '/t04w_240_4', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(158, '/t04w_240_4', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(159, '/t04w_240_5', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(160, '/t04w_240_5', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(161, '/t04w_240_5', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(162, '/t04w_240_5', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]