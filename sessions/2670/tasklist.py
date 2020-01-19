tasks = [
    # Generated on 2020-01-19 18:00:58.821086, contains telemetry from sessions 2668 to 2670.
    # The session starts on 2020-01-19 20:38:00+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234, 1284, 1334, 1384, 559, 609]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 547, 597, 647, 697]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 571, 621, 671, 721, 771, 821]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 541, 591, 641, 691, 741, 791, 841, 891, 941]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [991, 1041, 1091, 1141, 1191, 1241, 1291, 1341, 1391, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1103, 1153, 1203, 1253, 1303, 1353, 1403, 565, 615, 665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1215, 1265, 1315, 1365, 1415, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1327, 1377]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(43, '/p09w_480_0', [80]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [364, 371, 377, 383, 389, 395, 401, 407, 414, 421, 427, 433, 439, 445, 451, 457, 464, 471]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [477, 483, 489, 495, 501, 507, 514, 521, 527, 533, 539, 545, 551, 557, 564, 571, 577, 583]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p08w_480_0', [37, 45, 47, 48, 53, 54, 57, 90, 91, 168]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]