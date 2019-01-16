tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

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

    # missings from 273
    [tc.DownloadFile(30, '/telemetry.previous', [1891, 1903, 1915, 1927, 1941, 1953, 1965, 1977, 1991, 2003, 2015, 2027, 2041, 2053, 2065, 2077]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [2091, 2103, 2115, 2127, 2141, 2153, 2165, 2177, 2191, 2203, 2215, 2227, 2241, 2253, 2265, 2277]), Send, WaitMode.Wait],
    
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1197, 1247, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1122, 1172, 1222, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1060, 1110, 1160, 1210, 1260, 234, 284, 334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [984, 1034, 1084, 1134, 1184, 1234, 204, 254, 304, 354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [904, 954, 1004, 1054, 1104, 1154, 1204, 1254, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 1 hi-res
    [tc.DownloadFile(60, '/p1_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p1_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p1_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p1_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p1_480_0', [i for i in range(92, 115, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_480_0', [i for i in range(115, 138, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p1_480_0', [i for i in range(138, 162, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 4 hi-res
    [tc.DownloadFile(70, '/p4_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p4_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p4_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p4_480_0', [i for i in range(69, 75, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # focia 5 hi-res
    [tc.DownloadFile(80, '/p5_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p5_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p5_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p5_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p5_480_0', [i for i in range(92, 115, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p5_480_0', [i for i in range(115, 138, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p5_480_0', [i for i in range(138, 161, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/p5_480_0', [i for i in range(161, 171, 1)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    
    # focia 3 hi-res
    [tc.DownloadFile(90, '/p3_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(91, '/p3_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/p3_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/p3_480_0', [i for i in range(69, 76, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]