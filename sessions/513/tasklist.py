tasks = [
    # Generated on 2019-02-20 22:28:05.168000, contains telemetry from sessions 510 to 513.
    # The session starts on 2019-02-21 10:40:03+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # 8th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_8'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2189, 2239, 2214, 2264, 2202, 2252, 2226, 2276, 2196, 2246, 2208, 2258, 2220, 2270, 2232]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [9, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 34, 84, 134, 184, 234, 284, 334, 384, 434, 484, 534, 584]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 22, 72, 122, 172]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1222, 1272, 1322, 1372, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [846, 896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396, 16, 66, 116, 166, 216, 266, 316, 366]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 1266, 1316, 1366]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 2, 52, 102, 152]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1202, 1252, 1302, 1352]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]