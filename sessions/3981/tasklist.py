tasks = [
    # Generated on 2020-08-09 08:47:34.539000, contains telemetry from sessions 3979 to 3981.
    # The session starts on 2020-08-09 11:08:11+02:00.

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
    [tc.DownloadFile(31, '/telemetry.previous', [1367, 1417, 1467, 1517, 1567, 1617, 1667, 1717, 1767, 1817, 1867, 1917, 1967, 2017, 2067, 2117, 2167, 2217, 2267, 1392]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [37, 87, 137, 187, 237, 287, 337, 12, 62, 112, 162, 212, 262, 312, 362, 0, 50, 100, 150, 200]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1442, 1492, 1542, 1592, 1642, 1692, 1742, 1792, 1842, 1892, 1942, 1992, 2042, 2092, 2142, 2192, 2242, 1380, 1430, 1480]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1530, 1580, 1630, 1680, 1730, 1780, 1830, 1880, 1930, 1980, 2030, 2080, 2130, 2180, 2230, 1404, 1454, 1504, 1554, 1604]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [250, 300, 350, 24, 74, 124, 174, 224, 274, 324, 374, 44, 94, 144, 194, 244, 294, 344, 6, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.previous', [1654, 1704, 1754, 1804, 1854, 1904, 1954, 2004, 2054, 2104, 2154, 2204, 2254, 1374, 1424, 1474, 1524, 1574, 1624, 1674]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1724, 1774, 1824, 1874, 1924, 1974, 2024, 2074, 2124, 2174, 2224, 2274, 1386, 1436, 1486, 1536, 1586, 1636, 1686, 1736]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [1786, 1836, 1886, 1936, 1986, 2036, 2086, 2136, 2186, 2236, 1398, 1448, 1498, 1548, 1598, 1648, 1698, 1748, 1798, 1848]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [106, 156, 206, 256, 306, 356, 18, 68, 118, 168, 218, 268, 318, 368, 30, 80, 130, 180, 230, 280]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1898, 1948, 1998, 2048, 2098, 2148, 2198, 2248, 1410, 1460, 1510, 1560, 1610, 1660, 1710, 1760, 1810, 1860, 1910, 1960]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.previous', [2010, 2060, 2110, 2160, 2210, 2260]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [330, 380]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(31, '/a_n_11_32_0', [53, 54, 55, 106]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/a_n_11_40_0', [61, 62, 84]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/a_n_11_41_0', [41]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/a_w_11_31_0', [61, 77, 78, 79, 81, 83, 85, 87, 88, 89, 90, 91, 93, 95, 96, 97]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/a_w_11_31_0', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/a_w_11_32_0', [20, 47, 48, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/a_w_11_40_0', [40, 41, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/a_w_11_40_0', [77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/a_w_11_40_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/a_w_11_40_0', [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/a_w_11_40_0', [131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/a_w_11_40_0', [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/a_w_11_41_0', [28, 40, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/a_w_11_41_0', [73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/a_w_11_42_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/a_w_11_42_0', [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/a_w_11_42_0', [72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/a_w_11_57_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/a_w_11_57_0', [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/a_w_11_58_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/a_w_11_58_0', [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), Send, WaitMode.Wait],
	[tc.DownloadFile(52, '/a_w_11_58_0', [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(53, '/a_w_11_59_0', [25, 26, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
	[tc.DownloadFile(54, '/a_w_11_59_0', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
	[tc.DownloadFile(55, '/a_w_12_59_0', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
	[tc.DownloadFile(56, '/a_w_12_59_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]), Send, WaitMode.Wait],
	[tc.DownloadFile(57, '/a_w_12_59_0', [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
	[tc.DownloadFile(58, '/a_w_12_59_0', [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(59, '/a_w_13_00_0', [70, 78, 81]), Send, WaitMode.Wait],
	[tc.DownloadFile(60, '/a_w_13_01_0', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]), Send, WaitMode.Wait],
	[tc.DownloadFile(61, '/a_w_13_01_0', [72, 73, 74, 75, 76, 80, 81, 103, 104, 105, 107, 108, 122, 125]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]