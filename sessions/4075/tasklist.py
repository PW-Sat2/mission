tasks = [
    # Generated on 2020-08-23 14:32:52.444657, contains telemetry from sessions 4074 to 4075.
    # The session starts on 2020-08-23 21:56:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(61, '/telemetry.current', [691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 716, 766]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 1466, 1516, 1566, 704, 754, 804, 854]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 1454, 1504, 1554, 728, 778, 828, 878, 928, 978]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 1478, 1528, 698, 748, 798, 848, 898, 948, 998, 1048, 1098]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/telemetry.current', [1148, 1198, 1248, 1298, 1348, 1398, 1448, 1498, 1548, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/telemetry.current', [1260, 1310, 1360, 1410, 1460, 1510, 1560, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/telemetry.current', [1372, 1422, 1472, 1522, 1572, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/telemetry.current', [1484, 1534]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [385, 492, 536, 548, 567, 598, 617, 660, 667]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/a_w_11_49_0', [100]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/a_w_11_50_0', [59, 98, 101]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/a_n_12_58_0', [75, 76, 111, 112, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/a_n_12_58_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/a_n_12_58_0', [147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_n_12_59_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_n_12_59_0', [78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_n_12_59_0', [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_n_12_59_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_n_12_59_0', [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_n_13_00_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_n_13_00_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_n_13_00_0', [93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_n_13_00_0', [109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_n_13_00_0', [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_11_51_0', [51, 52, 53, 71, 76, 81, 101, 102, 103, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_12_59_0', [15, 16, 17, 18, 45, 48, 49, 50, 56, 57, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_12_59_0', [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_12_59_0', [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_12_59_0', [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_12_59_0', [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/a_w_12_59_0', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/a_w_13_00_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/a_w_13_00_0', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/a_w_13_00_0', [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/a_w_13_00_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/a_w_13_00_0', [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/a_w_13_00_0', [105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/a_w_13_00_0', [123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/a_w_13_00_0', [141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]