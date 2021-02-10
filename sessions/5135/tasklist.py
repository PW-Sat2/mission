tasks = [
    # Generated on 2021-02-10 13:01:55.066370, contains telemetry from sessions 5133 to 5135.
    # The session starts on 2021-02-10 21:37:55+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1244, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1219, 1269, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1157, 1207, 1257, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1131, 1181, 1231, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1101, 1151, 1201, 1251, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1063, 1113, 1163, 1213, 1263, 275, 325, 375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1025, 1075, 1125, 1175, 1225, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1037, 1087, 1137, 1187, 1237]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(40, '/telemetry.previous', [1244, 1249, 1253, 1254, 1258, 1259, 1264, 1269, 1273, 1274, 1278, 1279, 1284, 1289, 1293, 1294, 1298, 1299, 1304]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1309, 1313, 1314, 1318, 1319, 1324, 1329, 1333, 1334, 1338, 1339, 1344, 1349, 1353, 1354, 1358, 1359, 1364, 1369]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [1373, 1374, 1378, 1379, 1384, 1389, 1393, 1394, 1398, 1399, 1404, 1409, 1413, 1414, 1418, 1419, 1424, 1429, 1433]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1434, 1438, 1439, 1444, 1448, 1449, 1453, 1454, 1458, 1459, 1464, 1469, 1473, 1474, 1478, 1479, 1484, 1489]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.previous', [1493, 1494, 1498, 1499, 1504, 1509, 1513, 1514, 1518, 1519, 1524, 1529, 1533, 1534, 1538, 1539, 1544, 1549]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1553, 1554, 1558, 1559, 1564, 1568, 1569, 1573, 1574, 1578, 1579, 1584, 1588, 1589, 1593, 1594, 1598, 1599]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]