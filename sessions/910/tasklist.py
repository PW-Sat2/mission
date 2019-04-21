tasks = [
    # Generated on 2019-04-21 12:34:05.502393, contains telemetry from sessions 908 to 910.
    # The session starts on 2019-04-21 20:00:34+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 572, 622]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [672, 722, 772, 822, 872, 922, 972, 1022, 1072, 1122, 1172, 1222, 1272, 1322, 1372, 1422, 560, 610, 660, 710]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [760, 810, 860, 910, 960, 1010, 1060, 1110, 1160, 1210, 1260, 1310, 1360, 1410, 584, 634, 684, 734, 784, 834]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 1434, 554, 604, 654, 704, 754, 804, 854, 904]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [954, 1004, 1054, 1104, 1154, 1204, 1254, 1304, 1354, 1404, 566, 616, 666, 716, 766, 816, 866, 916, 966, 1016]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1066, 1116, 1166, 1216, 1266, 1316, 1366, 1416, 578, 628, 678, 728, 778, 828, 878, 928, 978, 1028, 1078, 1128]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1178, 1228, 1278, 1328, 1378, 1428, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1290, 1340, 1390, 1440]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.RemoveFile(38, 'suns_ps_4'), Send, WaitMode.NoWait],
    [tc.RemoveFile(39, 'suns_ps_4_sec'), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
