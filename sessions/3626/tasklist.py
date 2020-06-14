tasks = [
    # Generated on 2020-06-14 12:58:55.804113, contains telemetry from sessions 3623 to 3626.
    # The session starts on 2020-06-14 21:54:55+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220, 1270, 1320, 1370, 1420, 1470]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1520, 1570, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 1145, 1195, 1245, 1295, 1345, 1395]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1445, 1495, 1545, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283, 1333]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1383, 1433, 1483, 1533, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107, 1157, 1207, 1257, 1307]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1357, 1407, 1457, 1507, 1557, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1277, 1327, 1377, 1427, 1477, 1527, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 1189]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1239, 1289, 1339, 1389, 1439, 1489, 1539, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 1101, 1151]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1201, 1251, 1301, 1351, 1401, 1451, 1501, 1551, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513, 1563]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(40, '/telemetry.previous', [1662, 1812]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p10_0', [23, 45]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p8_0', [69, 70]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p9_0', [32, 35, 38, 40]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/t3w_0', [46, 88]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/t4n_0', [21, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/t4w_0', [17, 51, 73]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/t5n_0', [20, 67, 131, 132, 152, 153]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/t5w_0', [37, 68, 70, 74, 100, 101]), Send, WaitMode.Wait],
    # missing from previous session end

    # When everything is downloaded, switch to deep-sleep
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(6), Send, WaitMode.Wait],


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]