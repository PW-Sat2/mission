tasks = [
    # Generated on 2019-03-12 16:21:34.270000, contains telemetry from sessions 640 to 642.
    # The session starts on 2019-03-12 19:47:18+01:00.

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
    [tc.DownloadFile(30, '/telemetry.current', [1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837, 1887, 1937, 1987, 2037, 2087]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [2137, 2187, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [2062, 2112, 2162, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [2000, 2050, 2100, 2150, 2200, 1174, 1224, 1274, 1324, 1374, 1424, 1474, 1524, 1574, 1624, 1674, 1724, 1774, 1824, 1874]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1924, 1974, 2024, 2074, 2124, 2174, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606, 1656, 1706]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1756, 1806, 1856, 1906, 1956, 2006, 2056, 2106, 2156, 1168, 1218, 1268, 1318, 1368, 1418, 1468, 1518, 1568, 1618, 1668]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1718, 1768, 1818, 1868, 1918, 1968, 2018, 2068, 2118, 2168, 1180, 1230, 1280, 1330, 1380, 1430, 1480, 1530, 1580, 1630]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]