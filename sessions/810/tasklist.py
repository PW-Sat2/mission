tasks = [
    # Generated on 2019-04-06 19:17:40.100382, contains telemetry from sessions 809 to 810.
    # The session starts on 2019-04-06 20:46:41+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    # missing photo chunk
    [tc.DownloadFile(29, '/p2_128_0', [10]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 372, 422]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [472, 522, 572, 622, 672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 360, 410, 460, 510]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [560, 610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 384, 434, 484, 534, 584, 634]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 354, 404, 454, 504, 554, 604, 654, 704]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [754, 804, 854, 904, 954, 1004, 1054, 1104, 1154, 1204, 366, 416, 466, 516, 566, 616, 666, 716, 766, 816]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [866, 916, 966, 1016, 1066, 1116, 1166, 1216, 378, 428, 478, 528, 578, 628, 678, 728, 778, 828, 878, 928]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [978, 1028, 1078, 1128, 1178, 1228, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1090, 1140, 1190, 1240]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # radfet download
    [tc.DownloadFile(20, '/radfet_10', range(0, 8)), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/radfet_10', range(8, 16)), Send, WaitMode.Wait],
    [tc.DownloadFile(22, '/radfet_10', range(16, 24)), Send, WaitMode.Wait],
    # radfet download end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]