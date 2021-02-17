tasks = [
    # Generated on 2021-02-17 10:57:38.173909, contains telemetry from sessions 5171 to 5172.
    # The session starts on 2021-02-17 12:14:52+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(41, '/telemetry.current', [1230, 1280, 1330, 1380, 1430, 1255, 1305, 1355, 1405, 1243, 1293, 1343, 1393, 1443, 1267, 1317, 1367, 1417, 1237, 1287]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1337, 1387, 1437, 1249, 1299, 1349, 1399, 1261, 1311, 1361, 1411, 1273, 1323, 1373, 1423]), Send, WaitMode.Wait],
    # auto-generated telemetry end
    
    [tc.DownloadFile(109, '/radfet_60', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [3, 10, 16, 22, 28, 34, 40, 46, 53, 60, 66, 72, 78, 84, 90, 96, 103, 110, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [122, 128, 134, 140, 146, 153, 160, 166, 172, 178, 184, 190, 196, 203, 210, 216, 222, 228, 234]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [240, 246, 253, 260, 266, 272, 278, 284, 290, 296, 303, 310, 316, 322, 328, 334, 340, 346, 353]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [360, 366, 372, 378, 384, 390, 396, 403, 410, 416, 422, 428, 434, 440, 446, 453, 460, 466, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [478, 484, 490, 496, 503, 510, 516, 522, 528, 534, 540, 546, 553, 560, 566, 572, 578, 584]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [590, 596, 603, 610, 616, 622, 628, 634, 640, 646, 653, 660, 666, 672, 678, 684, 690, 696]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [703, 710, 716, 722, 728, 734, 740, 746, 753, 760, 766, 772, 778, 784, 790, 796, 803, 810]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [816, 822, 828, 834, 840, 846, 853, 860, 866, 872, 878, 884, 890, 896, 903, 910, 916, 922]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [928, 934, 940, 946, 953, 960, 966, 972, 978, 984, 990, 996, 1003, 1010, 1016, 1022, 1028, 1034]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1040, 1046, 1053, 1060, 1066, 1072, 1078, 1084, 1090, 1096, 1103, 1110, 1116, 1122, 1128, 1134, 1140, 1146]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1153, 1160, 1166, 1172, 1178, 1184, 1190, 1196, 1203, 1210, 1216, 1222, 1228, 1234, 1240, 1246, 1253, 1260]), Send, WaitMode.Wait],
    # missing from previous session end

    [tc.DownloadFile(104, '/p0_n_p480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p0_n_p480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p0_n_p480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p0_n_p480_0', [i for i in range(60, 80, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p0_n_p480_0', [i for i in range(80, 98, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(100, '/p1_w_p480_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p1_w_p480_0', [i for i in range(20, 40, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p1_w_p480_0', [i for i in range(40, 60, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p1_w_p480_0', [i for i in range(60, 71, 1)]), Send, WaitMode.Wait],
    
    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]