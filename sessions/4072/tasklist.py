tasks = [
    # Generated on 2020-08-23 00:32:50.813000, contains telemetry from sessions 4070 to 4072.
    # The session starts on 2020-08-23 11:10:09+02:00.

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
    [tc.DownloadFile(52, '/telemetry.previous', [1360, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960, 2010, 2060, 2110, 2160, 2210, 2260, 1385]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [30, 80, 130, 180, 230, 280, 330, 5, 55, 105, 155, 205, 255, 305, 355, 43, 93, 143, 193, 243]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.previous', [1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085, 2135, 2185, 2235, 1373, 1423, 1473]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973, 2023, 2073, 2123, 2173, 2223, 2273, 1397, 1447, 1497, 1547]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.current', [293, 343, 17, 67, 117, 167, 217, 267, 317, 367, 37, 87, 137, 187, 237, 287, 337, 49, 99, 149]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [1597, 1647, 1697, 1747, 1797, 1847, 1897, 1947, 1997, 2047, 2097, 2147, 2197, 2247, 1367, 1417, 1467, 1517, 1567, 1617]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.previous', [1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267, 1379, 1429, 1479, 1529, 1579, 1629, 1679]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1391, 1441, 1491, 1541, 1591, 1641, 1691, 1741]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [199, 249, 299, 349, 11, 61, 111, 161, 211, 261, 311, 361, 23, 73, 123, 173, 223, 273, 323, 373]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [1791, 1841, 1891, 1941, 1991, 2041, 2091, 2141, 2191, 2241, 1403, 1453, 1503, 1553, 1603, 1653, 1703, 1753, 1803, 1853]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.previous', [1903, 1953, 2003, 2053, 2103, 2153, 2203, 2253]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [1206, 1218, 1230, 1256, 1268, 1280, 1294, 1306, 1318, 1330, 1344, 1356, 1368, 1380, 1394, 1406]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_11_49_0', [100]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_11_50_0', [22, 23, 24, 26, 27, 29, 31, 32, 33, 34, 38, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_11_50_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_11_50_0', [63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 77, 78, 89, 98, 99, 100]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_11_50_0', [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_11_51_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_11_51_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_11_51_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/a_w_11_51_0', [94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/a_w_11_51_0', [111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/a_w_12_59_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/a_w_12_59_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/a_w_12_59_0', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/a_w_13_00_0', [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/a_w_13_00_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/a_w_13_00_0', [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]