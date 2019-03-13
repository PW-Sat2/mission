tasks = [
    # Generated on 2019-03-13 20:09:34.758000, contains telemetry from sessions 648 to 649.
    # The session starts on 2019-03-13 21:24:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [236, 286, 336, 386, 436, 261, 311, 361, 411, 249, 299, 349, 399, 449, 273, 323, 373, 423, 243, 293]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [343, 393, 443, 255, 305, 355, 405, 455, 267, 317, 367, 417, 279, 329, 379, 429]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.DownloadFile(40, '/telemetry.previous', [46, 53, 65, 77, 89, 103, 115, 127, 139, 153, 165, 177, 189, 203, 215, 227, 239, 253, 265, 277]), Send, WaitMode.Wait],
	[tc.DownloadFile(41, '/telemetry.previous', [289, 303, 315, 327, 339, 353, 365, 377, 389, 403, 415, 427, 439, 453, 465, 477, 489, 503, 515, 521]), Send, WaitMode.Wait],
	[tc.DownloadFile(42, '/telemetry.previous', [527, 539, 546, 553, 565, 577, 589, 603, 615, 627, 639, 653, 665, 677, 689, 703, 715, 727, 739, 753]), Send, WaitMode.Wait],
	[tc.DownloadFile(43, '/telemetry.previous', [765, 777, 789, 803, 815, 827, 839, 853, 865, 877, 889, 903, 915, 927, 939, 953, 965, 977, 989, 1003]), Send, WaitMode.Wait],
	[tc.DownloadFile(44, '/telemetry.previous', [1015, 1027, 1039, 1046, 1053, 1065, 1077, 1089, 1096, 1103, 1115, 1127, 1139, 1153, 1165, 1177, 1189, 1196, 1203, 1215]), Send, WaitMode.Wait],
	[tc.DownloadFile(45, '/telemetry.previous', [1227, 1239, 1253, 1265, 1277, 1289, 1303, 1315, 1327, 1333, 1339, 1353, 1365, 1377, 1389, 1396, 1403, 1415, 1427, 1433]), Send, WaitMode.Wait],
	[tc.DownloadFile(46, '/telemetry.previous', [1439, 1446, 1453, 1465, 1477, 1489, 1503, 1515, 1527, 1533, 1539, 1553, 1565, 1577, 1589, 1603, 1615, 1627, 1639]), Send, WaitMode.Wait],
	[tc.DownloadFile(47, '/telemetry.previous', [1646, 1653, 1665, 1677, 1689, 1703, 1715, 1727, 1739, 1746, 1753, 1765, 1777, 1783, 1789, 1803, 1815, 1827, 1833]), Send, WaitMode.Wait],
	[tc.DownloadFile(48, '/telemetry.previous', [1839, 1853, 1865, 1877, 1889, 1903, 1915, 1927, 1933, 1939, 1953, 1965, 1977, 1983, 1989, 2003, 2015, 2027, 2039]), Send, WaitMode.Wait],
	[tc.DownloadFile(49, '/telemetry.previous', [2053, 2065, 2077, 2089, 2103, 2115, 2127, 2139, 2153, 2165, 2177, 2189, 2203, 2215, 2227, 2239, 2253, 2265, 2277]), Send, WaitMode.Wait],
	[tc.DownloadFile(50, '/telemetry.current', [9, 23, 29, 35, 47, 59, 73, 85, 97, 109, 135]), Send, WaitMode.Wait],
	[tc.DownloadFile(51, '/telemetry.current', [147, 159, 173, 185, 197, 209, 223, 235, 247, 253, 259]), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]