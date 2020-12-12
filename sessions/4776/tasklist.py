tasks = [
    # Generated on 2020-12-12 15:32:34.411000, contains telemetry from sessions 4775 to 4776.
    # The session starts on 2020-12-12 21:07:14+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(38, '/telemetry.current', [349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099, 1149, 1199, 374, 424]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124, 1174, 362, 412, 462, 512, 562]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 386, 436, 486, 536, 586, 636, 686]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [856, 906, 956, 1006, 1056, 1106, 1156, 1206, 368, 418, 468, 518, 568, 618, 668, 718, 768, 818, 868, 918]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [968, 1018, 1068, 1118, 1168, 1218, 380, 430, 480, 530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1080, 1130, 1180, 392, 442, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942, 992, 1042, 1092, 1142, 1192]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # auto-generated file download start
    [tc.DownloadFile(45, '/b_w_p480_3_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/b_w_p480_3_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/b_w_p480_3_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/b_w_p480_3_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/b_w_p480_3_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/b_w_p480_3_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/b_w_p480_3_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/b_w_p480_3_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/b_w_p480_3_0', [150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/b_n_p480_3_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/b_n_p480_3_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/b_n_p480_3_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/b_n_p480_3_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/b_n_p480_3_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/b_n_p480_3_0', [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/b_n_p480_3_0', [119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/b_n_p480_3_0', [138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156]), Send, WaitMode.Wait],
    # auto-generated file download end

    # missing from previous session start
    [tc.DownloadFile(30, '/b_n_p480_1_0', [80]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/b_n_p480_2_0', [80, 81, 82, 83]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/b_w_p480_1_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/b_w_p480_1_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/b_w_p480_1_0', [115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/b_w_p480_1_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/b_w_p480_1_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/b_w_p480_2_0', [80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]