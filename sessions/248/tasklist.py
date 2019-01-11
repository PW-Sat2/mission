tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1883, 1933, 1983, 2033, 2083, 2133, 2183, 2233, 1908, 1958, 2008, 2058, 2108, 2158, 2208, 2258, 1896, 1946, 1996, 2046]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1003, 1053, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [928, 978, 1028, 1078, 16, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [2096, 2146, 2196, 2246, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1890, 1940, 1990, 2040, 2090, 2140, 2190, 2240]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [816, 866, 916, 966, 1016, 1066, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [740, 790, 840, 890, 940, 990, 1040, 1090, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1926, 1976, 2026, 2076]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 34, 84, 134, 184, 234, 284, 334, 384]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 46, 96, 146, 196, 246, 296]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [2126, 2176, 2226, 2276]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(100, '/p4_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]