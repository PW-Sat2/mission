tasks = [
    # Generated on 2021-02-22 23:07:15.037000, contains telemetry from sessions 5203 to 5204.
    # The session starts on 2021-02-23 00:14:05+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(47, '/telemetry.current', [2001, 2051, 2101, 2151, 2201, 2026, 2076, 2126, 2176, 2014, 2064, 2114, 2164, 2214, 2038, 2088, 2138, 2188, 2008, 2058]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [2108, 2158, 2208, 2020, 2070, 2120, 2170, 2032, 2082, 2132, 2182, 2044, 2094, 2144, 2194]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [82, 729, 893, 905, 917, 929, 943, 949, 955, 967, 979, 993, 1005, 1017, 1029, 1055, 1067, 1079, 1105, 1117]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1129, 1155, 1167, 1179, 1205, 1217, 1229, 1243, 1255, 1267, 1279, 1293, 1305, 1317, 1329, 1343, 1355, 1367, 1379]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1393, 1405, 1417, 1423, 1429, 1443, 1455, 1467, 1479, 1493, 1505, 1517, 1529, 1543, 1555, 1567, 1573, 1579, 1593]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1605, 1617, 1623, 1629, 1643, 1655, 1667, 1679, 1693, 1705, 1717, 1729, 1743, 1755, 1767, 1779, 1793, 1805, 1817]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1829, 1843, 1855, 1867, 1879, 1893, 1905, 1917, 1929, 1943, 1955, 1967, 1979, 1993, 2005, 2017, 2023, 2029, 2043]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2028, 2160]), Send, WaitMode.Wait],

    [tc.DownloadFile(61, '/o1_w_128_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/o1_w_128_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/o1_w_128_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/o1_w_128_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/o1_w_128_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/o1_w_128_0', range(100, 120)), Send, WaitMode.Wait],

    [tc.DownloadFile(81, '/o1_n_480_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/o1_n_480_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/o1_n_480_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/o1_n_480_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/o1_n_480_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/o1_n_480_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/o1_n_480_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/o1_n_480_0', range(140, 160)), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/o1_n_480_0', range(160, 180)), Send, WaitMode.Wait],

    [tc.DownloadFile(36, '/pw_p10_0', [28, 29, 30, 39, 52, 53, 54, 55, 56, 57, 58, 65, 66, 67, 68, 69]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/pw_p14_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/pw_p14_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/pw_p14_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/pw_p19_0', [2, 4, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/pw_p19_0', [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/pw_p19_0', [46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/pw_p6_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/pw_p6_0', [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/pw_p6_0', [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/pw_p6_0', [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]