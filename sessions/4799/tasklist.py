tasks = [
    # Generated on 2020-12-16 10:21:35.824065, contains telemetry from sessions 4798 to 4799.
    # The session starts on 2020-12-16 11:38:53+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(57, '/telemetry.current', [440, 490, 540, 590, 640, 465, 515, 565, 615, 453, 503, 553, 603, 653, 477, 527, 577, 627, 447, 497]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [547, 597, 647, 459, 509, 559, 609, 471, 521, 571, 621, 483, 533, 583, 633]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [1, 13, 39, 51, 63, 89, 101, 113, 127, 139, 151, 163, 177, 189]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [201, 213, 220, 227, 239, 251, 263, 277, 289, 301, 313, 327, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [351, 357, 363, 377, 389, 401, 407, 413, 427, 439, 451, 463, 477]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1464, 1494, 1582, 1669, 1681, 1688, 1693, 1719, 1731, 1743, 1769, 1781, 1793, 1819, 1831]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1843, 1869, 1881, 1893, 1919, 1931, 1943, 1969, 1981, 1993, 2019, 2031, 2043, 2069, 2081]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2093, 2107, 2119, 2131, 2143, 2157, 2169, 2181, 2193, 2207, 2219, 2231, 2243, 2257, 2269]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/w_17_43_0', [55, 61, 62, 63, 64, 65, 66, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/w_17_43_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/w_17_43_0', [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/w_17_43_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/w_17_45_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/w_17_45_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/w_17_45_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/w_17_45_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/w_17_45_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/w_17_45_0', [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/w_17_45_0', [124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/w_17_46_0', [28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/w_17_46_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/w_17_46_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/w_17_46_0', [82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/w_17_46_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/w_17_46_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/w_17_46_0', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/w_17_46_0', [153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/x_14_42_0', [6, 7, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/x_17_11_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
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