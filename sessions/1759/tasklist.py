tasks = [
    # Generated on 2019-09-01 01:19:45.407000, contains telemetry from sessions 1758 to 1759.
    # The session starts on 2019-09-01 10:11:32+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(89, '/telemetry.previous', [1545, 1595, 1645, 1695, 1745, 1795, 1845, 1895, 1945, 1995, 2045, 2095, 2145, 2195, 2245, 1570, 1620, 1670, 1720, 1770]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/telemetry.current', [15, 65, 115, 165, 215, 265, 315, 365, 40, 90, 140, 190, 240, 290, 340, 390, 28, 78, 128, 178]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/telemetry.previous', [1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220, 2270, 1558, 1608, 1658, 1708, 1758, 1808, 1858, 1908, 1958, 2008]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/telemetry.previous', [2058, 2108, 2158, 2208, 2258, 1582, 1632, 1682, 1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1552]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/telemetry.current', [228, 278, 328, 378, 2, 52, 102, 152, 202, 252, 302, 352, 22, 72, 122, 172, 222, 272, 322, 372]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/telemetry.previous', [1602, 1652, 1702, 1752, 1802, 1852, 1902, 1952, 2002, 2052, 2102, 2152, 2202, 2252, 1564, 1614, 1664, 1714, 1764, 1814]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/telemetry.previous', [1864, 1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/telemetry.current', [34, 84, 134, 184, 234, 284, 334, 384, 46, 96, 146, 196, 246, 296, 346, 396, 8, 58, 108, 158]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/telemetry.previous', [2126, 2176, 2226, 2276, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/telemetry.current', [208, 258, 308, 358]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_14_sec', [479, 483, 484, 495, 498, 499, 500, 501, 502, 503, 505, 506, 507, 508, 509]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_14_sec', [510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_14_sec', [525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_14_sec', [540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_13_sec', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_13_sec', [11, 14, 21, 67, 95, 96, 98, 149, 186, 197]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_12_sec', [171]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1367, 1374, 1380, 1386, 1392, 1398, 1404, 1410, 1417, 1430, 1436, 1448, 1454, 1460]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1467, 1474, 1480, 1486, 1492, 1498, 1504, 1510, 1517, 1530, 1536, 1542, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_14', [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_14', [143, 144, 146, 147, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_14', [166, 167, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_14', [187, 188, 189, 190, 191, 192, 193, 195, 196, 197, 199, 415, 447, 449, 491, 492, 493, 494, 495, 497]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_14', [498, 499, 500, 501, 502, 504, 505, 506, 507, 508, 509, 561, 562, 564, 568, 569, 570, 600, 601, 604]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_14', [605, 691, 692, 693, 694, 695, 697, 698, 699, 700, 701, 702, 704, 705, 706, 707, 708, 709, 711, 712]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_14', [713, 714, 715, 717, 718, 719, 720, 721, 723, 724, 725, 726, 727, 729, 730, 731, 732, 733, 735, 736]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_14', [737, 738, 739, 741, 742, 743, 744, 745, 747, 748, 749, 750, 751, 752, 754, 755, 756, 757, 758, 759]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_14', [761, 762, 763, 764, 765, 767, 768, 769, 770, 771, 773, 774, 775, 776, 777, 779, 780, 781, 782, 783]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_14', [785, 786, 787, 788, 789, 791, 792, 793, 794, 795, 797, 798, 799, 800, 801, 802, 804, 805, 806, 807]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_14', [808, 809, 811, 812, 813, 814, 815, 817, 818, 819, 820, 821, 823, 824, 825, 826, 827, 829, 830, 831]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_14', [832, 833, 835, 836, 837, 838, 839, 841, 842, 843, 844, 845, 847, 848, 849, 850, 851, 852, 854, 855]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_14', [856, 857, 858, 859, 861, 862, 863, 864, 865, 867, 868, 869, 870, 871, 873, 874, 875, 876, 877, 879]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_14', [880, 881, 882, 883, 885, 886, 887, 888, 889, 891, 892, 893, 894, 895, 897, 898, 899, 900, 901, 902]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_14', [904, 905, 906, 907, 908, 909, 911, 912, 913, 914, 915, 917, 918, 919, 920, 921, 923, 924, 925, 926]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_14', [927, 929, 930, 931, 932, 933, 935, 936, 937, 938, 939, 941, 942, 943, 944, 945, 947, 948, 949, 950]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_14', [951, 952, 954, 955, 956, 957, 958, 959, 961, 962, 963, 964, 965, 967, 968, 969, 970, 971, 973, 974]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_14', [975, 976, 977, 979, 980, 981, 982, 983, 985, 986, 987, 988, 989, 991, 992, 993, 994, 995, 997, 998]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_14', [999, 1000, 1001, 1002, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1014, 1015, 1017, 1018, 1019, 1020, 1021]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_14', [1023, 1024, 1025, 1026, 1027, 1029, 1030, 1031, 1032, 1033, 1035, 1036, 1037, 1038, 1039, 1041, 1042, 1043, 1044, 1045]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_14', [1047, 1048, 1049, 1050, 1051, 1052, 1054, 1055, 1056, 1057, 1058, 1059, 1061, 1062, 1063, 1064, 1065, 1067, 1068, 1069]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_14', [1070, 1071, 1073, 1074, 1075, 1076, 1077, 1079, 1080, 1081, 1082, 1083, 1085, 1086, 1087, 1088, 1089, 1091, 1092, 1093]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_14', [1094, 1095, 1097, 1098, 1099, 1100, 1101, 1102, 1104, 1105, 1106, 1107, 1108, 1109, 1111, 1112, 1113, 1114, 1115, 1117]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_14', [1118, 1119, 1120, 1121, 1123, 1124, 1125, 1126, 1127, 1129, 1130, 1131, 1132, 1133, 1135, 1136, 1137, 1138, 1139, 1141]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_14', [1142, 1143, 1144, 1145, 1147, 1148, 1149, 1150, 1151, 1152, 1154, 1155, 1156, 1157, 1158, 1159, 1161, 1162, 1163, 1164]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_14', [1165, 1167, 1168, 1169, 1170, 1171, 1173, 1174, 1175, 1176, 1177, 1179, 1180, 1181, 1182, 1183, 1185, 1186, 1187, 1188]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_14', [1189, 1191, 1192, 1193, 1194, 1195, 1197, 1198, 1199, 1200, 1201, 1202, 1204, 1205, 1206, 1207, 1208, 1209, 1211, 1212]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_14', [1213, 1214, 1215, 1217, 1218, 1219, 1220, 1221, 1223, 1224, 1225, 1226, 1227, 1229, 1230, 1231, 1232, 1233, 1235, 1236]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/suns_ps_14', [1237, 1238, 1239, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/suns_ps_14', [1258, 1259, 1260, 1261, 1262, 1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1275, 1276, 1277]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/suns_ps_14', [1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1292, 1293, 1294, 1295, 1296, 1297]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/suns_ps_14', [1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/suns_ps_14', [1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332, 1333, 1334, 1335, 1336, 1337]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/suns_ps_14', [1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1346, 1347, 1348, 1349, 1350, 1351, 1352, 1353, 1354, 1355, 1356, 1357]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/suns_ps_14', [1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/suns_ps_14', [1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393, 1394, 1395, 1396, 1397]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/suns_ps_14', [1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/suns_ps_14', [1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/suns_ps_14', [1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453, 1454, 1455, 1456]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/suns_ps_14', [1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473, 1474, 1475]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/suns_ps_14', [1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493, 1494]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/suns_ps_14', [1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/suns_ps_14', [1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/suns_ps_14', [1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/suns_ps_14', [1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/suns_ps_14', [1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/suns_ps_14', [1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/suns_ps_14', [1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/suns_ps_14', [1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/suns_ps_14', [1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]