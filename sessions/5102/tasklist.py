tasks = [
    # Generated on 2021-02-04 21:32:17.634926, contains telemetry from sessions 5101 to 5102.
    # The session starts on 2021-02-04 22:10:03+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(34, '/telemetry.current', [1307, 1357, 1407, 1457, 1507, 1332, 1382, 1432, 1482, 1320, 1370, 1420, 1470, 1344, 1394, 1444, 1494, 1314, 1364, 1414]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1464, 1514, 1326, 1376, 1426, 1476, 1338, 1388, 1438, 1488, 1350, 1400, 1450, 1500]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [492, 504, 516, 528, 542, 554, 566, 578, 592, 604, 616, 628, 642, 654, 666, 678, 692, 704, 716, 728]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [742, 754, 766, 778, 792, 804, 816, 828, 842, 854, 866, 872, 878, 892, 904, 916, 922, 928, 942, 954]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [966, 972, 978, 992, 1004, 1016, 1022, 1028, 1042, 1054, 1066, 1072, 1078, 1092, 1104, 1116, 1122, 1128, 1142, 1154]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1166, 1172, 1178, 1192, 1204, 1216, 1222, 1228, 1242, 1254, 1266, 1272, 1278, 1292, 1304, 1316, 1322, 1328, 1342]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]