tasks = [
    # Generated on 2019-07-14 17:28:25.769000, contains telemetry from sessions 1467 to 1468.
    # The session starts on 2019-07-14 20:50:43+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340, 1390, 565, 615]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 1415, 553, 603, 653, 703]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 1353, 1403, 577, 627, 677, 727, 777, 827]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427, 547, 597, 647, 697, 747, 797, 847, 897]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 1397, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1059, 1109, 1159, 1209, 1259, 1309, 1359, 1409, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1171, 1221, 1271, 1321, 1371, 1421, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1283, 1333, 1383]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]