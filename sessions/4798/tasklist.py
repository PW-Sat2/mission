tasks = [
    # Generated on 2020-12-16 00:33:03.479000, contains telemetry from sessions 4797 to 4798.
    # The session starts on 2020-12-16 10:06:32+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(52, '/telemetry.previous', [1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1675, 1725, 1775, 1825, 1875, 1925, 1975]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 45, 95, 145, 195, 245, 295, 345, 395, 445, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [2025, 2075, 2125, 2175, 2225, 2275, 1663, 1713, 1763, 1813, 1863, 1913, 1963, 2013, 2063, 2113, 2163, 2213, 2263, 1687]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [83, 133, 183, 233, 283, 333, 383, 433, 7, 57, 107, 157, 207, 257, 307, 357, 407, 457, 27, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087, 2137, 2187, 2237, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [2107, 2157, 2207, 2257, 1669, 1719, 1769, 1819, 1869, 1919, 1969, 2019, 2069, 2119, 2169, 2219, 2269, 1681, 1731, 1781]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [127, 177, 227, 277, 327, 377, 427, 477, 39, 89, 139, 189, 239, 289, 339, 389, 439, 1, 51, 101]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [1831, 1881, 1931, 1981, 2031, 2081, 2131, 2181, 2231, 1693, 1743, 1793, 1843, 1893, 1943, 1993, 2043, 2093, 2143, 2193]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [151, 201, 251, 301, 351, 401, 451, 13, 63, 113, 163, 213, 263, 313, 363, 413, 463]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [2243, 1464, 1494, 1582, 1688]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/w_17_43_0', [55, 61, 62, 63, 64, 65, 66, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/w_17_43_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/w_17_43_0', [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/w_17_43_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/w_17_45_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/w_17_45_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/w_17_45_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/w_17_45_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/w_17_45_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/w_17_45_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/w_17_45_0', [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/w_17_46_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/w_17_46_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/w_17_46_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/w_17_46_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/w_17_46_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/w_17_46_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/w_17_46_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/w_17_46_0', [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/x_14_42_0', [6, 7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/x_17_11_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end
    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]