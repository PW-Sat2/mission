tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

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
    [tc.DownloadFile(30, '/telemetry.previous', [607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307, 1357, 1407, 1457, 1507, 1557]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [1607, 1657, 1707, 1757, 1807, 1857, 1907, 1957, 2007, 2057, 2107, 2157, 2207, 2257, 632, 682, 732, 782, 832, 882]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 1632, 1682, 1732, 1782, 1832, 1882]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.previous', [1932, 1982, 2032, 2082, 2132, 2182, 2232, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1002, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [1270, 1320, 1370, 1420, 1470, 1520, 1570, 1620, 1670, 1720, 1770, 1820, 1870, 1920, 1970, 2020, 2070, 2120, 2170, 2220]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2270, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [990, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [1594, 1644, 1694, 1744, 1794, 1844, 1894, 1944, 1994, 2044, 2094, 2144, 2194, 2244, 614, 664, 714, 764, 814, 864]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [964, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.previous', [914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314, 1364, 1414, 1464, 1514, 1564, 1614, 1664, 1714, 1764, 1814, 1864]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.previous', [1914, 1964, 2014, 2064, 2114, 2164, 2214, 2264, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [984, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.previous', [1226, 1276, 1326, 1376, 1426, 1476, 1526, 1576, 1626, 1676, 1726, 1776, 1826, 1876, 1926, 1976, 2026, 2076, 2126, 2176]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.previous', [2226, 2276, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 1488]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [996, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 908]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.previous', [1538, 1588, 1638, 1688, 1738, 1788, 1838, 1888, 1938, 1988, 2038, 2088, 2138, 2188, 2238, 650, 700, 750, 800, 850]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [958, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.previous', [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450, 1500, 1550, 1600, 1650, 1700, 1750, 1800, 1850]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [1900, 1950, 2000, 2050, 2100, 2150, 2200, 2250]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [970]), Send, WaitMode.Wait],
    # auto-generated telemetry end

	# Remove photos
	[tc.RemoveFile(200, '/p10_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(201, '/p1_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(202, '/p4_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(203, '/p5_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(204, '/p6_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(205, '/p8_480_0'), Send, WaitMode.Wait],
	[tc.RemoveFile(206, '/p9_480_0'), Send, WaitMode.Wait],
	
	[tc.ListFiles(207, '/'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
