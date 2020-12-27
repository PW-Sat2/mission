tasks = [
    # Generated on 2020-12-27 14:03:56.523910, contains telemetry from sessions 4866 to 4868.
    # The session starts on 2020-12-27 21:23:04+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(42, '/telemetry.current', [477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 1427]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1477, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152, 1202, 1252, 1302, 1352, 1402]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1452, 1502, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990, 1040, 1090, 1140, 1190, 1240, 1290, 1340]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [1390, 1440, 1490, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014, 1064, 1114, 1164, 1214, 1264, 1314]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [1364, 1414, 1464, 1514, 484, 534, 584, 634, 684, 734, 784, 834, 884, 934, 984, 1034, 1084, 1134, 1184, 1234]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1284, 1334, 1384, 1434, 1484, 496, 546, 596, 646, 696, 746, 796, 846, 896, 946, 996, 1046, 1096, 1146, 1196]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [1246, 1296, 1346, 1396, 1446, 1496, 508, 558, 608, 658, 708, 758, 808, 858, 908, 958, 1008, 1058, 1108, 1158]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [1208, 1258, 1308, 1358, 1408, 1458, 1508, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 1020, 1070, 1120]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1170, 1220, 1270, 1320, 1370, 1420, 1470]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/telemetry.current', [24, 124, 130, 242, 248, 477, 484, 490, 496, 502, 508, 514, 520, 527]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [534, 540, 546, 552, 558, 564, 570, 577, 584, 590, 596, 602, 608, 614]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [620, 627, 634, 640, 646, 652, 658, 664, 670, 677, 684, 690, 696]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.previous', [1716, 2134, 2160, 2172]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/a_w_p480_11_32_0', [90, 108, 114, 140]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/a_w_p480_11_40_0', [55, 57, 81]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/a_w_p480_11_52_0', [29, 55, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/a_w_p480_11_56_0', [67]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/a_w_p480_12_00_0', [19, 38]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/a_w_p480_12_04_0', [99, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/a_w_p480_12_04_0', [127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/a_w_p480_12_04_0', [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start

    # auto-generated file download end


    # auto-generated file remove start

    # auto-generated file remove end
    [tc.SendBeacon(), Send, WaitMode.Wait],

    ["Set bootslots for deep_sleep.", Print, WaitMode.NoWait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]