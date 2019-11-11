tasks = [
    # Generated on 2019-11-11 13:58:51.852000, contains telemetry from sessions 2217 to 2218.
    # The session starts on 2019-11-11 20:08:56+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(70, '/telemetry.current', [35, 85, 135, 185, 235, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885, 60, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/telemetry.current', [160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 48, 98, 148, 198]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/telemetry.current', [248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 72, 122, 172, 222, 272, 322]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/telemetry.current', [372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 42, 92, 142, 192, 242, 292, 342, 392]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/telemetry.current', [442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 54, 104, 154, 204, 254, 304, 354, 404, 454, 504]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/telemetry.current', [554, 604, 654, 704, 754, 804, 854, 904, 66, 116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/telemetry.current', [666, 716, 766, 816, 866, 916, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/telemetry.current', [778, 828, 878]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.previous', [2176, 2182, 2232, 2270]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2, 9, 16, 22, 28, 34, 40, 46, 52, 59, 66, 72, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1342, 1510, 1610, 1660, 1672, 1722, 1760, 1810, 1860, 1910, 1960, 1980, 2117]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t08w_480_0', [75]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t13w_480_0', [115, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t21n_480_0', [35, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t22w_480_0', [38, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t19n_480_0', [17, 18, 48, 50, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t19n_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t17w_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t17w_480_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t17w_480_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t17w_480_0', [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/t17w_480_0', [84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t10w_480_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t10w_480_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t10w_480_0', [130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t10w_480_0', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t15n_480_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/t15n_480_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/t15n_480_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/t15n_480_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/t18n_480_0', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/t18n_480_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/t18n_480_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/t18n_480_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/t18w_480_0', [19, 20, 21, 33, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/t18w_480_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/t18w_480_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/t18w_480_0', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/t21w_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/t21w_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/t21w_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/t21w_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/t07w_480_0', [51, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/t07w_480_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t07w_480_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t14w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t14w_480_0', [79, 87, 97, 99, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 131, 138]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t14w_480_0', [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]