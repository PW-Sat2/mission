tasks = [
    # Generated on 2021-02-04 13:32:58.406333, contains telemetry from sessions 5100 to 5101.
    # The session starts on 2021-02-04 20:41:09+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [485, 535, 585, 635, 685, 735, 785, 835, 885, 935, 985, 1035, 1085, 1135, 1185, 1235, 1285, 1335, 510, 560]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [610, 660, 710, 760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 498, 548, 598, 648, 698]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [748, 798, 848, 898, 948, 998, 1048, 1098, 1148, 1198, 1248, 1298, 1348, 522, 572, 622, 672, 722, 772, 822]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 492, 542, 592, 642, 692, 742, 792, 842, 892, 942]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [992, 1042, 1092, 1142, 1192, 1242, 1292, 1342, 504, 554, 604, 654, 704, 754, 804, 854, 904, 954, 1004, 1054]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1104, 1154, 1204, 1254, 1304, 516, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016, 1066, 1116, 1166, 1216]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1266, 1316, 528, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128, 1178, 1228, 1278, 1328]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    ,
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]