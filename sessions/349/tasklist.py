tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [248, 298, 348, 398, 448, 498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1248, 1298, 1348, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 273, 323, 373, 423, 473, 523, 573, 623, 673, 723]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [773, 823, 873, 923, 973, 1023, 1073, 1123, 1173, 1223, 1273, 1323, 1373, 1423, 1473, 1523, 1573, 1623, 1673, 1723]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911, 961, 1011, 1061, 1111, 1161, 1211]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1261, 1311, 1361, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 285, 335, 385, 435, 485, 535, 585, 635, 685, 735]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 267, 317, 367, 417, 467, 517, 567, 617, 667, 717]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1267, 1317, 1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [279, 329, 379, 429, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1279, 1329, 1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 291, 341, 391, 441, 491, 541, 591, 641, 691, 741]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [791, 841, 891, 941, 991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(117, '/p3_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/p3_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/p3_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/p3_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/p3_480_0', [i for i in range(80, 89, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(122, '/p7_480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/p7_480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/p7_480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/p7_480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/p7_480_0', [i for i in range(80, 86, 1)]), Send, WaitMode.Wait],

    # Remove downloaded low photos
    [tc.RemoveFile(200, '/p7_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(201, '/p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(202, '/p9_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(203, '/p10_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(204, '/p2_480_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]