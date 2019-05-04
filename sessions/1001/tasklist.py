tasks = [
    # Generated on 2019-04-05 21:21:02.361000

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

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # 11th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_12'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry from previous sessions
    [tc.DownloadFile(30, '/telemetry.current', [176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1176, 1226, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1101, 1151, 1201, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1039, 1089, 1139, 1189, 1239, 213, 263, 313, 363, 413, 463, 513, 563, 613, 663, 713, 763, 813, 863, 913]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [963, 1013, 1063, 1113, 1163, 1213, 183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [883, 933, 983, 1033, 1083, 1133, 1183, 1233, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', range(150, 176, 3)), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Low res photos download
	[tc.DownloadFile(103, '/p3_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p4_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(106, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p5_128_0', [i for i in range(18, 29, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(108, '/p6_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p6_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p7_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p7_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(112, '/p8_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p8_128_0', [i for i in range(18, 28, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(114, '/p9_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p9_128_0', [i for i in range(18, 31, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(116, '/p10_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/p10_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]