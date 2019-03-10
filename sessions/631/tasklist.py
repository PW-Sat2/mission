tasks = [
    # Generated on 2019-03-10 19:57:57.485000, contains telemetry from sessions 628 to 631.
    # The session starts on 2019-03-10 21:12:40+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS A
    [tc.RawI2C(3, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1422, 1472, 1522, 1572, 1622, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 435, 485, 535, 585, 635, 685, 735, 785, 835, 885]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 459, 509, 559, 609, 659]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609, 1659]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329, 1379]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1429, 1479, 1529, 1579, 1629, 441, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041, 1091, 1141]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 465, 515, 565, 615, 665]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565, 1615]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove files
    [tc.RemoveFile(100, 'p1_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(102, 'p2_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(104, 'p3_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(106, 'p4_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(108, 'p5_480_0' ), Send, WaitMode.Wait],

    [tc.RemoveFile(110, 'p6_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(112, 'p7_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(114, 'p8_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(116, 'p9_480_0' ), Send, WaitMode.NoWait],
    [tc.RemoveFile(118, 'p10_480_0'), Send, WaitMode.Wait],

    [tc.ListFiles(120, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]