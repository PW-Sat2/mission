tasks = [
    # Generated on 2020-11-08 13:06:13.145000, contains telemetry from sessions 4563 to 4564.
    # The session starts on 2020-11-08 20:25:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(41, '/telemetry.current', [510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 535, 585]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 523, 573, 623, 673]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [723, 773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 547, 597, 647, 697, 747, 797]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 517, 567, 617, 667, 717, 767, 817, 867, 917]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1079, 1129, 1179, 1229, 1279, 1329, 1379, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1191, 1241, 1291, 1341, 1391, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1303, 1353]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/n_w_6_0', [130, 134, 135, 136, 137, 138, 139, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/n_w_6_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/n_w_7_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/n_w_7_0', [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/n_w_7_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/n_w_7_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/n_w_8_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/n_w_8_0', [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/n_w_8_0', [52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/n_w_8_0', [69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/n_w_8_0', [86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]