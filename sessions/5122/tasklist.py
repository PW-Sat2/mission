tasks = [
    # Generated on 2021-02-08 00:28:39.040000, contains telemetry from sessions 5121 to 5122.
    # The session starts on 2021-02-08 11:24:33+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1472, 1522, 1572, 1622, 1672, 1722, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1197, 1247, 1297, 1347, 1397, 1447, 1497, 1547, 1597, 1647, 1697, 485, 535, 585, 635, 685, 735, 785, 835, 885]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 1385, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 509, 559, 609]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 1459, 1509, 1559, 1609]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1659, 1709, 479, 529, 579, 629, 679, 729, 779, 829, 879, 929, 979, 1029, 1079, 1129, 1179, 1229, 1279, 1329]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1379, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 491, 541, 591, 641, 691, 741, 791, 841, 891, 941, 991, 1041]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1091, 1141, 1191, 1241, 1291, 1341, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 503, 553, 603, 653, 703, 753, 803]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 515, 565]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 1465, 1515, 1565]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1615, 1665, 1715, 295, 314, 326, 332, 338, 345, 364, 376, 388, 402]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [408, 414, 426, 438, 452, 464, 476, 488, 502, 514]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]