tasks = [
    # Generated on 2021-02-06 00:35:19.703000, contains telemetry from sessions 5109 to 5110.
    # The session starts on 2021-02-06 10:02:06+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(48, '/telemetry.previous', [2069, 2119, 2169, 2219, 2269, 2094, 2144, 2194, 2244, 2082, 2132, 2182, 2232, 2106, 2156, 2206, 2256, 2076, 2126, 2176]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [39, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 14, 64, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 2, 52, 102, 152, 202]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 26, 76, 126, 176, 226, 276, 326]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 46, 96, 146, 196, 246, 296, 346, 396, 446]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.previous', [2226, 2276, 2088, 2138, 2188, 2238, 2100, 2150, 2200, 2250, 2112, 2162, 2212, 2262]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [496, 546, 596, 646, 696, 746, 796, 846, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.current', [608, 658, 708, 758, 808, 858, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [720, 770, 820, 870, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.current', [832, 882]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/p0_n_p480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p0_n_p480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p0_n_p480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p0_n_p480_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p0_n_p480_0', [74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p0_n_p480_0', [92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p0_n_p480_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p0_n_p480_0', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]