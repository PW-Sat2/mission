tasks = [
    # Generated on 2020-11-22 23:44:07.162062, contains telemetry from sessions 4650 to 4655.
    # The session starts on 2020-11-23 10:39:28+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(43, '/telemetry.previous', [1665, 1715, 1765, 1815, 1865, 1915, 1965, 2015, 2065, 2115, 2165, 2215, 2265, 1690, 1740, 1790, 1840, 1890, 1940, 1990]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 10, 60, 110, 160, 210, 260, 310]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [2040, 2090, 2140, 2190, 2240, 1678, 1728, 1778, 1828, 1878, 1928, 1978, 2028, 2078, 2128, 2178, 2228, 2278, 1702, 1752]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [360, 410, 460, 510, 560, 610, 660, 48, 98, 148, 198, 248, 298, 348, 398, 448, 498, 548, 598, 648]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.previous', [1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1672, 1722, 1772, 1822, 1872, 1922, 1972, 2022, 2072, 2122]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 42, 92, 142, 192, 242, 292]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.previous', [2172, 2222, 2272, 1684, 1734, 1784, 1834, 1884, 1934, 1984, 2034, 2084, 2134, 2184, 2234, 1696, 1746, 1796, 1846, 1896]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [342, 392, 442, 492, 542, 592, 642, 4, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504, 554, 604]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [654, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 28, 78, 128, 178, 228]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [1946, 1996, 2046, 2096, 2146, 2196, 2246, 1708, 1758, 1808, 1858, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [278, 328, 378, 428, 478, 528, 578, 628]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [508, 520, 545, 570, 602, 652, 708, 758, 832, 1320, 1370]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/n_w_1_0', [17, 69, 70, 71, 83, 159, 160, 161, 162, 163]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/n_w_2_0', [53, 61, 63, 64, 65, 68, 72, 74, 78, 129, 136, 137, 150, 151, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n_w_3_0', [19, 26, 27, 49, 50, 51, 62, 63, 64, 124, 134]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n_w_4_0', [73, 83, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n_w_5_0', [50, 51, 52, 68, 69, 70, 81, 82, 83, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/n_w_6_0', [41, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/n_w_6_0', [69, 78, 79, 80, 83, 86, 87, 89, 93, 94, 98, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/n_w_7_0', [33, 35, 61, 62, 63, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/n_w_7_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/n_w_8_0', [19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/n_w_8_0', [66, 67, 70, 106, 117, 118, 126, 127, 132, 133, 137, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/n_w_8_0', [147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161]), Send, WaitMode.Wait],
    # missing from previous session end


    ["Set bootslots for deep_sleep.", Print, WaitMode.Wait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],



    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
