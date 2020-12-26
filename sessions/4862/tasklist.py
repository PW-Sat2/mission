tasks = [
    # Generated on 2020-12-26 15:13:42.947000, contains telemetry from sessions 4861 to 4862.
    # The session starts on 2020-12-26 20:24:35+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(96, '/telemetry.current', [171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 196, 246]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.current', [296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 184, 234, 284, 334]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 208, 258, 308, 358, 408, 458]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/telemetry.current', [508, 558, 608, 658, 708, 758, 808, 858, 908, 958, 1008, 178, 228, 278, 328, 378, 428, 478, 528, 578]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/telemetry.current', [628, 678, 728, 778, 828, 878, 928, 978, 1028, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.current', [740, 790, 840, 890, 940, 990, 1040, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.current', [852, 902, 952, 1002, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.current', [1014]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [30, 74, 105, 155, 162]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a_n_p480_11_56_0', [0, 1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 18, 20, 21, 22, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_w_p480_11_22_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_n_p480_11_22_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_n_p480_11_22_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_n_p480_11_22_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_n_p480_11_22_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_n_p480_11_26_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_n_p480_11_26_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_n_p480_11_26_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_n_p480_11_26_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_n_p480_11_32_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_n_p480_11_32_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_n_p480_11_32_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_n_p480_11_32_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_n_p480_11_40_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_n_p480_11_40_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_n_p480_11_40_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_n_p480_11_40_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_n_p480_11_52_0', [13, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_n_p480_11_52_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_n_p480_11_52_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_n_p480_11_52_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_n_p480_11_56_0', [24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_n_p480_11_56_0', [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_n_p480_11_56_0', [62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a_n_p480_12_00_0', [8, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a_n_p480_12_00_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a_n_p480_12_00_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_n_p480_12_00_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a_n_p480_12_04_0', [2, 3, 11, 12, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/a_n_p480_12_04_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/a_n_p480_12_04_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/a_n_p480_12_04_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/a_w_p480_11_22_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/a_w_p480_11_22_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/a_w_p480_11_22_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/a_w_p480_11_22_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/a_w_p480_11_26_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/a_w_p480_11_26_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/a_w_p480_11_26_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/a_w_p480_11_26_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/a_w_p480_11_32_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/a_w_p480_11_32_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/a_w_p480_11_32_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/a_w_p480_11_32_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/a_w_p480_11_40_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/a_w_p480_11_40_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/a_w_p480_11_40_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/a_w_p480_11_40_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/a_w_p480_11_52_0', [7, 8, 11, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/a_w_p480_11_52_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/a_w_p480_11_52_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/a_w_p480_11_52_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/a_w_p480_11_56_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/a_w_p480_11_56_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/a_w_p480_11_56_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/a_w_p480_11_56_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/a_w_p480_12_00_0', [10, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/a_w_p480_12_00_0', [34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/a_w_p480_12_00_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/a_w_p480_12_00_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/a_w_p480_12_04_0', [10, 11, 12, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/a_w_p480_12_04_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/a_w_p480_12_04_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/a_w_p480_12_04_0', [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(108, '/a_w_p480_11_22_0', [80, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/a_n_p480_11_22_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/a_n_p480_11_22_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/a_n_p480_11_22_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/a_n_p480_11_22_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/a_n_p480_11_26_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/a_n_p480_11_26_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/a_n_p480_11_26_0', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/a_n_p480_11_26_0', [140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/a_w_p480_11_32_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/a_w_p480_11_32_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/a_w_p480_11_32_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/a_w_p480_11_32_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/a_w_p480_11_40_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(150, '/a_n_p480_11_40_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/a_n_p480_11_40_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/a_n_p480_11_40_0', [108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/a_n_p480_11_40_0', [126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/a_n_p480_11_40_0', [143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]), Send, WaitMode.Wait],
    [tc.DownloadFile(171, '/a_n_p480_11_56_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(194, '/a_n_p480_12_00_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91]), Send, WaitMode.Wait],
    [tc.DownloadFile(185, '/a_w_p480_12_04_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]), Send, WaitMode.Wait],
    [tc.DownloadFile(186, '/a_w_p480_12_04_0', [91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(187, '/a_w_p480_12_04_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(190, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(189, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]