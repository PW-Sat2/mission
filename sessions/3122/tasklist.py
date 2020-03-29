tasks = [
    # Generated on 2020-03-29 09:30:57.740316, contains telemetry from sessions 3121 to 3122.
    # The session starts on 2020-03-29 10:10:50+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 1875, 1925, 1975, 2025, 2075, 2125, 2175, 2225, 2275, 1400]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [45, 95, 145, 195, 20, 70, 120, 170, 220, 8, 58, 108, 158, 208, 32, 82, 132, 182, 2, 52]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850, 1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250, 1388, 1438, 1488]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 1412, 1462, 1512, 1562, 1612]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1662, 1712, 1762, 1812, 1862, 1912, 1962, 2012, 2062, 2112, 2162, 2212, 2262, 1382, 1432, 1482, 1532, 1582, 1632, 1682]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1732, 1782, 1832, 1882, 1932, 1982, 2032, 2082, 2132, 2182, 2232, 1394, 1444, 1494, 1544, 1594, 1644, 1694, 1744, 1794]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [102, 152, 202, 14, 64, 114, 164, 214, 26, 76, 126, 176, 226, 38, 88, 138, 188]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 1406, 1456, 1506, 1556, 1606, 1656, 1706, 1756, 1806, 1856, 1906]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1956, 2006, 2056, 2106, 2156, 2206, 2256, 1418, 1468, 1518, 1568, 1618, 1668, 1718, 1768, 1818, 1868, 1918, 1968, 2018]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2068, 2118, 2168, 2218, 2268]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Carefully waste some session time
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]