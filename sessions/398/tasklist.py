tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

	[tc.DownloadFile(30, '/telemetry.previous', [485, 491, 497, 509, 515, 521, 535, 541, 547, 559, 565, 571, 585, 591, 597, 609, 615, 621, 635, 641]), Send, WaitMode.Wait],
	[tc.DownloadFile(31, '/telemetry.previous', [647, 653, 659, 665, 671, 685, 691, 697, 703, 709, 715, 721, 735, 741, 747, 753, 759, 765, 771, 785]), Send, WaitMode.Wait],
	[tc.DownloadFile(32, '/telemetry.previous', [791, 797, 803, 809, 815, 821, 835, 841, 847, 853, 859, 865, 871, 885, 891, 897, 903, 909, 915, 921]), Send, WaitMode.Wait],
	[tc.DownloadFile(33, '/telemetry.previous', [935, 941, 947, 953, 959, 965, 971, 985, 991, 997, 1003, 1009, 1015, 1021, 1035, 1041, 1047, 1053, 1059]), Send, WaitMode.Wait],
	[tc.DownloadFile(34, '/telemetry.previous', [1065, 1071, 1085, 1091, 1097, 1103, 1109, 1115, 1121, 1135, 1141, 1147, 1153, 1159, 1165, 1171, 1185, 1191, 1197]), Send, WaitMode.Wait],
	[tc.DownloadFile(35, '/telemetry.previous', [1203, 1209, 1215, 1221, 1235, 1241, 1247, 1253, 1259, 1265, 1271, 1285, 1291, 1297, 1303, 1309, 1315, 1321, 1335]), Send, WaitMode.Wait],
	[tc.DownloadFile(36, '/telemetry.previous', [1341, 1347, 1353, 1359, 1365, 1371, 1385, 1391, 1397, 1403, 1409, 1415, 1421, 1435, 1441, 1447, 1453, 1459, 1465]), Send, WaitMode.Wait],
	[tc.DownloadFile(37, '/telemetry.previous', [1471, 1485, 1491, 1497, 1503, 1509, 1515, 1521, 1535, 1541, 1547, 1553, 1559, 1565, 1571, 1578, 1585, 1591, 1597]), Send, WaitMode.Wait],
	[tc.DownloadFile(38, '/telemetry.previous', [1603, 1609, 1615, 1621, 1635, 1641, 1647, 1653, 1659, 1665, 1671, 1685, 1691, 1697, 1703, 1709, 1715, 1721, 1735]), Send, WaitMode.Wait],
	[tc.DownloadFile(39, '/telemetry.previous', [1741, 1747, 1753, 1759, 1765, 1771, 1785, 1791, 1797, 1803, 1809, 1815, 1821, 1835, 1841, 1847, 1853, 1859, 1865]), Send, WaitMode.Wait],
	[tc.DownloadFile(40, '/telemetry.previous', [1871, 1885, 1891, 1897, 1903, 1909, 1915, 1921, 1935, 1941, 1947, 1953, 1959, 1965, 1971, 1985, 1991, 1997, 2003]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.previous', [2009, 2015, 2021, 2035, 2041, 2047, 2053, 2059, 2065, 2071, 2085, 2091, 2097, 2103, 2109, 2115, 2121, 2135, 2141]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.previous', [2147, 2153, 2159, 2165, 2171, 2185, 2191, 2197, 2203, 2209, 2215, 2221, 2235, 2241, 2247, 2253, 2259, 2265, 2271]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.current', [5, 11, 17, 23, 29, 35, 41, 48, 55, 61, 67, 73, 79, 85, 91, 98, 105, 111]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.current', [117, 123, 129, 135, 141, 148, 155, 161, 167, 173, 179, 185, 191, 198, 205, 211, 217, 223]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.current', [229, 235, 241, 248, 255, 261, 267, 273, 279, 285, 291, 298, 305, 311, 317, 323, 329, 335]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/telemetry.current', [341, 348, 355, 361, 367, 373, 379, 385, 391, 398, 405, 411, 417, 423, 429, 435, 441, 448]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/telemetry.current', [455, 461, 467, 473, 479, 485, 491, 498, 505, 511, 517, 523, 529, 535, 541, 548, 555]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/telemetry.current', [561, 567, 573, 579, 585, 591, 598, 605, 611, 617, 623, 629, 635, 641, 648, 655, 661]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/telemetry.current', [667, 673, 679, 685, 691, 698, 705, 711, 717, 723, 729, 735, 741, 748, 755, 761, 767]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/telemetry.current', [773, 779, 785, 791, 798, 805, 811, 817, 823, 829, 835, 841, 848, 855, 861, 867, 873]), Send, WaitMode.Wait]
]
