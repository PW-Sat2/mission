tasks = [
    # Generated on 2019-02-18 20:03:08.548000, contains telemetry from sessions 497 to 498.
    # The session starts on 2019-02-18 21:20:06+01:00.

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

    # randomized missings from session 497
    [tc.DownloadFile(30, '/telemetry.previous', [1950, 2200, 1906, 1324, 1730, 1800, 1650, 1456, 1962, 2250, 1406, 1850, 1830, 1450, 2124, 1656]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [400,676,206,532,356,144,782,50,170,282,306,426,876,1256,1194,1344]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1300,1206,826,1326,1088,1270,1076,820,220,956,1226,320,1156,482,1006]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1512, 2112, 1386, 1480, 1924, 2086, 1624, 1336, 1356, 2012, 1606, 2230, 2186, 2118, 1912, 2000]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [194,1332,476,970,744,1150,6,544,456,1200,56,806,526,906,588,494]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [156,656,626,732,276,932,756,1070,950,232,382,82,332,594,1020]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1506, 2106, 2136, 1400, 1680, 1556, 2074, 2024, 1530, 2056, 2162, 2036, 2080, 1300, 2050, 1836]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1044,0,106,256,470,1026,582,1106,200,682,976,406,994,670,1050,506]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [688,500,444,1276,450,326,432,94,376,1094,70,1238,700,344,632]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [1718, 2100, 1562, 1956, 1936, 1986, 1712, 1612, 1586, 1786, 1886, 1636, 1700, 1306, 1756, 1574]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1120,832,920,270,1282,570,900,420,1244,644,1056,926,1182,1144,988]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [1380, 1474, 1824, 2212, 1362, 1812, 1536, 1500, 2180, 1412, 1524, 1874, 1462, 2236, 1930, 2262]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1000,76,1032,132,20,726,944,244,606,32,738,882,982,182,1126,1132]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1630, 1436, 1774, 2130, 1806, 2274, 1750, 2224, 1550, 1862, 1330, 1762, 1350, 1900, 1430, 1486]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [350,706,1138,1220,294,394,870,520,850,750,1320,1038,800,650,770,150]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1980, 1706, 1780, 1674, 1374, 1662, 2030, 1424, 1686, 1312, 1600, 2150, 2206, 1880, 1724, 1580]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [620,638,300,44,1082,370,250,576,550,788,844,1176,556,694,794,894]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [100,538,1250,720,856,1170,26,1306,600,776,1100,888,1232,1294,1188,120]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [2156, 2062, 1974, 2006, 2174, 1856, 1418, 1736]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(50, '/telemetry.current', [1310, 1360, 1410, 1460, 1510, 1335, 1385, 1435, 1485, 1323, 1373, 1423, 1473, 1523, 1347, 1397, 1447, 1497, 1317, 1367]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [1417, 1467, 1517, 1329, 1379, 1429, 1479, 1529, 1341, 1391, 1441, 1491, 1353, 1403, 1453, 1503]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Remove photo files
    [tc.RemoveFile(101, 'p2_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(102, 'p2_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(103, 'p3_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(104, 'p4_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(105, 'p4_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(106, 'p5_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(107, 'p5_480_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(108, 'p8_128_0'), Send, WaitMode.Wait],
    [tc.RemoveFile(109, 'p10_480_0'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]