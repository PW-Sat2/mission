tasks = [
    # Generated on 2019-09-01 13:04:44.941000, contains telemetry from sessions 1760 to 1761.
    # The session starts on 2019-09-01 13:21:39+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [523, 573, 623, 673, 723, 548, 598, 648, 698, 536, 586, 636, 686, 736, 560, 610, 660, 710, 530, 580]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [630, 680, 730, 542, 592, 642, 692, 742, 554, 604, 654, 704, 566, 616, 666, 716]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/suns_ps_14_sec', [479, 500, 501, 502, 506, 551, 553]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/suns_ps_14', [191, 199, 882, 1295, 1296, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_14', [1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331, 1332]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_14', [1333, 1334, 1335, 1336, 1337, 1338, 1339, 1340, 1341, 1342, 1343, 1344, 1345, 1347, 1348, 1349, 1350, 1351, 1352, 1353]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_14', [1354, 1355, 1356, 1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_14', [1374, 1375, 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_14', [1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_14', [1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_14', [1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449, 1450, 1451, 1452, 1453]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_14', [1454, 1455, 1456, 1457, 1458, 1459, 1460, 1461, 1462, 1463, 1464, 1465, 1466, 1467, 1468, 1469, 1470, 1471, 1472, 1473]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_14', [1474, 1475, 1476, 1477, 1478, 1479, 1480, 1481, 1482, 1483, 1484, 1485, 1486, 1487, 1488, 1489, 1490, 1491, 1492, 1493]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_14', [1494, 1495, 1496, 1497, 1498, 1499, 1500, 1501, 1502, 1503, 1504, 1505, 1506, 1507, 1508, 1509, 1510, 1511, 1512, 1513]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_14', [1514, 1515, 1516, 1517, 1518, 1519, 1520, 1521, 1522, 1523, 1524, 1525, 1526, 1527, 1528, 1529, 1530, 1531, 1532]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_14', [1533, 1534, 1535, 1536, 1537, 1538, 1539, 1540, 1541, 1542, 1543, 1544, 1545, 1546, 1547, 1548, 1549, 1550, 1551]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_14', [1552, 1553, 1554, 1555, 1556, 1557, 1558, 1559, 1560, 1561, 1562, 1563, 1564, 1565, 1566, 1567, 1568, 1569, 1570]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_14', [1571, 1572, 1573, 1574, 1575, 1576, 1577, 1578, 1579, 1580, 1581, 1582, 1583, 1584, 1585, 1586, 1587, 1588, 1589]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_14', [1590, 1591, 1592, 1593, 1594, 1595, 1596, 1597, 1598, 1599, 1600, 1601, 1602, 1603, 1604, 1605, 1606, 1607, 1608]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_14', [1609, 1610, 1611, 1612, 1613, 1614, 1615, 1616, 1617, 1618, 1619, 1620, 1621, 1622, 1623, 1624, 1625, 1626, 1627]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_14', [1628, 1629, 1630, 1631, 1632, 1633, 1634, 1635, 1636, 1637, 1638, 1639, 1640, 1641, 1642, 1643, 1644, 1645, 1646]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_14', [1647, 1648, 1649, 1650, 1651, 1652, 1653, 1654, 1655, 1656, 1657, 1658, 1659, 1660, 1661, 1662, 1663, 1664, 1665]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]