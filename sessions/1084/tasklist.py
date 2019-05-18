tasks = [
    # Generated on 2019-05-18 13:52:05.776000, contains telemetry from sessions 1083 to 1084.
    # The session starts on 2019-05-18 21:06:34+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(37, '/telemetry.current', [351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151, 1201, 376, 426]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176, 1226, 364, 414, 464, 514]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 388, 438, 488, 538, 588, 638]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 358, 408, 458, 508, 558, 608, 658, 708]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 1208, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [870, 920, 970, 1020, 1070, 1120, 1170, 1220, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [982, 1032, 1082, 1132, 1182, 1232, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1094, 1144, 1194]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p8_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [197, 209, 234, 271]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p9_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/p10_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(45, '/p1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p1_480_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p1_480_0', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p1_480_0', [54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p1_480_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p2_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p2_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p2_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p2_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p2_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p2_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p2_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/p2_480_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/p2_480_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/p3_480_0', [0]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]