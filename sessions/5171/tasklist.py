tasks = [
    # Generated on 2021-02-17 10:27:20.825154, contains telemetry from sessions 5170 to 5171.
    # The session starts on 2021-02-17 10:44:42+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [3, 53, 103, 153, 203, 253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1003, 1053, 1103, 1153, 1203, 1253, 28, 78, 128, 178, 228, 278, 328, 378, 428, 478, 528, 578, 628, 678]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 16, 66, 116, 166, 216, 266, 316, 366, 416]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [466, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216, 40, 90, 140, 190]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1240, 10, 60, 110, 160, 210, 260, 310, 360, 410, 460, 510, 560, 610, 660, 710, 760, 810, 860, 910]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [960, 1010, 1060, 1110, 1160, 1210, 1260, 22, 72, 122, 172, 222, 272, 322, 372, 422, 472, 522, 572, 622]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 34, 84, 134, 184, 234, 284, 334, 384]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [434, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 46, 96, 146]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [196, 246, 296, 346, 396, 446, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 1096, 1146]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1196, 1246]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]