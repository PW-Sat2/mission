tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848, 1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248, 1423, 1473]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [18, 68, 118, 168, 218, 268, 318, 43, 93, 143, 193, 243, 293, 343, 31, 81, 131, 181, 231, 281]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 1411, 1461, 1511, 1561]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1611, 1661, 1711, 1761, 1811, 1861, 1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1435, 1485, 1535, 1585, 1635, 1685]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [331, 5, 55, 105, 155, 205, 255, 305, 355, 25, 75, 125, 175, 225, 275, 325, 37, 87, 137, 187]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1967, 2017, 2067, 2117, 2167, 2217, 2267, 1429, 1479, 1529, 1579, 1629, 1679, 1729, 1779, 1829, 1879, 1929, 1979, 2029]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [237, 287, 337, 49, 99, 149, 199, 249, 299, 349, 11, 61, 111, 161, 211, 261, 311]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2079, 2129, 2179, 2229, 2279, 1441, 1491, 1541, 1591, 1641, 1691, 1741, 1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2191, 2241]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]