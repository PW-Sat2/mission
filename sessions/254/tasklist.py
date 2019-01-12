tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2233, 2258, 2246, 2270, 2240, 2252, 2264, 2276]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328, 1378, 1428, 16, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [116, 166, 216, 266, 316, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1116, 1166, 1216, 1266, 1316, 1366, 1416, 40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 1440, 10, 60, 110, 160]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1210, 1260, 1310, 1360, 1410, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622, 672, 722]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 34, 84, 134, 184, 234, 284]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [334, 384, 434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1334, 1384, 1434, 46, 96, 146, 196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [896, 946, 996, 1046, 1096, 1146, 1196, 1246, 1296, 1346, 1396]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]