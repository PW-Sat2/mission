tasks = [
    # Generated on 2019-10-05 18:24:25.080000, contains telemetry from sessions 1966 to 1968.
    # The session starts on 2019-10-05 20:43:05+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 196, 246]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 184, 234, 284, 334]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 208, 258, 308, 358, 408, 458]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [508, 558, 608, 658, 708, 758, 808, 858, 908, 958, 1008, 1058, 178, 228, 278, 328, 378, 428, 478, 528]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [690, 740, 790, 840, 890, 940, 990, 1040, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [802, 852, 902, 952, 1002, 1052, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [914, 964, 1014]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(38, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(39, '/p1_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p1_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p1_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p1_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p1_480_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p1_480_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138]), Send, WaitMode.Wait],

    [tc.DownloadFile(46, '/p2_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p2_480_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p2_480_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p2_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]