tasks = [
    # Generated on 2019-06-16 10:01:07.770000, contains telemetry from sessions 1279 to 1281.
    # The session starts on 2019-06-16 11:02:13+02:00.

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
    [tc.DownloadFile(30, '/telemetry.previous', [1392, 1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 1417, 1467]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [12, 62, 112, 162, 212, 262, 312, 362, 412, 37, 87, 137, 187, 237, 287, 337, 387, 25, 75, 125]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267, 1405, 1455, 1505, 1555]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1605, 1655, 1705, 1755, 1805, 1855, 1905, 1955, 2005, 2055, 2105, 2155, 2205, 2255, 1429, 1479, 1529, 1579, 1629, 1679]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [175, 225, 275, 325, 375, 49, 99, 149, 199, 249, 299, 349, 399, 19, 69, 119, 169, 219, 269, 319]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [1729, 1779, 1829, 1879, 1929, 1979, 2029, 2079, 2129, 2179, 2229, 2279, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1799, 1849, 1899, 1949, 1999, 2049, 2099, 2149, 2199, 2249, 1411, 1461, 1511, 1561, 1611, 1661, 1711, 1761, 1811, 1861]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [369, 419, 31, 81, 131, 181, 231, 281, 331, 381, 43, 93, 143, 193, 243, 293, 343, 393, 5, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1911, 1961, 2011, 2061, 2111, 2161, 2211, 2261, 1423, 1473, 1523, 1573, 1623, 1673, 1723, 1773, 1823, 1873, 1923, 1973]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2023, 2073, 2123, 2173, 2223, 2273, 1435, 1485, 1535, 1585, 1635, 1685, 1735, 1785, 1835, 1885, 1935, 1985, 2035, 2085]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2135, 2185, 2235]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [105, 155, 205, 255, 305, 355, 405]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/p7_480_0', [16, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p2_480_0', [37, 45, 46, 60, 61, 66, 70, 71, 72, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/p2_480_0', [74, 77, 78, 79, 80, 81, 82, 83, 84, 85]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p3_480_0', [25]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(42, '/suns_ps_7', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_7', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_7', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_7', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_7', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_7', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_7', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_7', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_7', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_7', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_7', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_7', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_7', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]