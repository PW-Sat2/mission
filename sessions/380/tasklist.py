tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # the first post-sail SunS experiment
    [tc.PerformSunSExperiment(3, 0, 20, 250, datetime.timedelta(seconds=5), 3, datetime.timedelta(seconds=10), 'suns_ps_1'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2047, 2097, 2147, 2197, 2247, 2072, 2122, 2172, 2222, 2272, 2060, 2110, 2160, 2210, 2260, 2084, 2134, 2184, 2234, 2054]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [17, 67, 117, 167, 217, 267, 317, 367, 417, 467, 517, 567, 617, 667, 717, 767, 817, 867, 917, 967]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1017, 1067, 1117, 1167, 1217, 42, 92, 142, 192, 242, 292, 342, 392, 442, 492, 542, 592, 642, 692, 742]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [792, 842, 892, 942, 992, 1042, 1092, 1142, 1192, 1242, 30, 80, 130, 180, 230, 280, 330, 380, 430, 480]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [530, 580, 630, 680, 730, 780, 830, 880, 930, 980, 1030, 1080, 1130, 1180, 1230, 4, 54, 104, 154, 204]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [254, 304, 354, 404, 454, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1254, 24, 74, 124, 174, 224, 274, 324, 374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2104, 2154, 2204, 2254, 2066, 2116, 2166, 2216, 2266, 2078, 2128, 2178, 2228, 2278, 2090, 2140, 2190, 2240]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [974, 1024, 1074, 1124, 1174, 1224, 36, 86, 136, 186, 236, 286, 336, 386, 436, 486, 536, 586, 636, 686]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [736, 786, 836, 886, 936, 986, 1036, 1086, 1136, 1186, 1236, 48, 98, 148, 198, 248, 298, 348, 398, 448]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [498, 548, 598, 648, 698, 748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248, 10, 60, 110, 160]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(200, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]