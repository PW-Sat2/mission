tasks = [
    # Generated on 2019-06-02 18:19:14.518000, contains telemetry from sessions 1186 to 1189.
    # The session starts on 2019-06-02 21:34:01+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],


    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 1163, 1213, 1263, 1313, 1363, 1413, 1463, 1513]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1563, 1613, 588, 638, 688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1488, 1538, 1588, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 1076, 1126, 1176, 1226, 1276, 1326, 1376]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1426, 1476, 1526, 1576, 1626, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1350, 1400, 1450, 1500, 1550, 1600, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120, 1170, 1220]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1270, 1320, 1370, 1420, 1470, 1520, 1570, 1620, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1182, 1232, 1282, 1332, 1382, 1432, 1482, 1532, 1582, 594, 644, 694, 744, 794, 844, 894, 944, 994, 1044, 1094]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [1144, 1194, 1244, 1294, 1344, 1394, 1444, 1494, 1544, 1594, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1106, 1156, 1206, 1256, 1306, 1356, 1406, 1456, 1506, 1556, 1606]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(103, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    # Get beacons from deep-sleep
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
