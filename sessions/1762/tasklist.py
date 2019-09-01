tasks = [
    # Generated on 2019-09-01 20:20:44.405000, contains telemetry from sessions 1761 to 1762.
    # The session starts on 2019-09-01 21:04:08+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(40, '/telemetry.current', [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 725, 775]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 713, 763, 813, 863]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563, 737, 787, 837, 887, 937, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 707, 757, 807, 857, 907, 957, 1007, 1057]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1331, 1381, 1431, 1481, 1531, 1581, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1443, 1493, 1543]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_14', [1470, 1471, 1472, 1473, 1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_14', [1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_14', [1510, 1511, 1512, 1513, 1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_14', [1530, 1531, 1532, 1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_14', [1550, 1551, 1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_14', [1570, 1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_14', [1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_14', [1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_14', [1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_14', [1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]