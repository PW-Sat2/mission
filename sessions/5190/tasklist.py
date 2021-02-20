tasks = [
    # Generated on 2021-02-20 15:27:13.972000, contains telemetry from sessions 5189 to 5190.
    # The session starts on 2021-02-20 20:57:08+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 334, 384]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 322, 372, 422, 472, 522]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 346, 396, 446, 496, 546, 596, 646, 696]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [746, 796, 846, 896, 946, 996, 1046, 1096, 1146, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [866, 916, 966, 1016, 1066, 1116, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1028, 1078, 1128, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(38, '/pw_p0_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/pw_p0_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/pw_p0_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/pw_p0_0', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/pw_p1_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/pw_p1_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pw_p1_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pw_p2_0', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/pw_p3_0', [0, 1, 2, 3, 4, 5, 6, 7, 8]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    [tc.RemoveFile(47, 'n01n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(48, 'n01w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(49, 'n02n_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(50, 'n02w_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(51, 'p0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(52, 'p1_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(53, 'p1_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(54, 'p1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(55, 'p2_n_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(56, 'p2_w_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(57, 'p5174_0_n_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(58, 'p5174_1_w_p480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(59, 'radfet_60'), Send, WaitMode.Wait],
    [tc.RemoveFile(60, 'radfet_61'), Send, WaitMode.Wait],
    [tc.ListFiles(61, '/'), Send, WaitMode.Wait],
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]