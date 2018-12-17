tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # Telemetry between session 82 and 83
    [tc.DownloadFile(3, '/telemetry.current', [i for i in range(1000, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(4, '/telemetry.current', [i for i in range(1006, 1200, 12)]), Send, WaitMode.Wait],

    # Missing chunks of high res photos
    [tc.DownloadFile(5, '/p7_480_0', [35]), Send, WaitMode.Wait], # retry until download

    # Delete Sun-ish and overexposed photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(10, '/p11_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(11, '/p13_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(12, '/p14_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(13, '/p15_480_0'), Send, WaitMode.Wait],

    [tc.RemoveFile(14, '/p16_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(15, '/p17_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(16, '/p18_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(17, '/p19_480_0'), Send, WaitMode.Wait],

    # Remove downloaded photos
    [tc.RemoveFile(18, '/p6_480_0'), Send, WaitMode.NoWait],
    # [tc.RemoveFile(19, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(20, '/p3_480_0'), Send, WaitMode.Wait],

    # Remove old RadFET exp
    [tc.ListFiles(25, '/radfet_2'), Send, WaitMode.Wait],
    # Remove downloaded suns exp data
    [tc.ListFiles(26, '/suns_4'), Send, WaitMode.Wait],

    [tc.ListFiles(27, '/'), Send, WaitMode.Wait],

    # Missing fourth SunS Experiment secondary data
    [tc.DownloadFile(30, '/suns_4_sec', [14, 15, 16, 34, 35, 36, 37, 40, 54, 55, 56, 71, 72, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_4_sec', [96, 100, 101, 102, 103, 104, 105, 106, 107, 112, 113, 122]), Send, WaitMode.Wait],
 
    # RadFET Exp data download
    [tc.DownloadFile(32, '/radfet_3', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],

    # More telemetry between session 82 and 83 (during RadFET exp)
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(1001, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(1002, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(1003, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [i for i in range(1004, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [i for i in range(1005, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [i for i in range(1007, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [i for i in range(1008, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [i for i in range(1009, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [i for i in range(1010, 1200, 12)]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [i for i in range(1011, 1200, 12)]), Send, WaitMode.Wait],

    # Missing telemetry chunks between session 81 and 82
    [tc.DownloadFile(103, '/telemetry.current', [98, 100, 6, 9, 15, 25, 28, 40, 46, 48, 56, 75, 125, 128, 134, 140, 146, 148, 171]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.current', [175, 198, 200, 234, 246, 284, 287, 296, 298, 331, 337, 346, 348, 350, 362, 365]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.current', [375, 381, 387, 396, 398, 400, 409, 412, 428, 431, 434, 437, 446, 448, 450, 462]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.current', [475, 484, 487, 498, 500, 509, 512, 515, 534, 546, 548, 550, 553, 562, 584, 590]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.current', [598, 600, 634, 648, 650, 696, 698, 700, 734, 746, 748, 771, 775, 798, 840, 846]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.current', [848, 859, 865, 890, 896, 898, 921, 928, 940, 946, 948, 959, 971, 990, 998, 1000]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/telemetry.previous', [2051, 2075, 2117, 2121, 2123, 2126, 2133, 2145, 2147, 2158, 2159, 2170, 2182, 2183, 2185, 2186]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.previous', [2198, 2206, 2207, 2219, 2231, 2234, 2239, 2243, 2255, 2263, 2267, 2021, 2279, 2035, 2039, 2043, 2047]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
