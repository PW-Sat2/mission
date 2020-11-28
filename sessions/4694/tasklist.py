tasks = [
    # Generated on 2020-11-29 00:18:51.180000, contains telemetry from sessions 4692 to 4694.
    # The session starts on 2020-11-29 09:52:59+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.DownloadFile(32, '/w_p480_0_0', [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171]), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(33, '/telemetry.current', [169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1169, 1219, 1269, 1319, 1369, 1419, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794, 844]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 1344, 1394, 1444, 182, 232, 282, 332, 382, 432, 482, 532]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 1332, 1382, 1432, 206, 256]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [306, 356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [1306, 1356, 1406, 1456, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [976, 1026, 1076, 1126, 1176, 1226, 1276, 1326, 1376, 1426, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 1338, 1388, 1438, 200, 250, 300, 350]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1400, 1450, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [1112, 1162, 1212, 1262, 1312, 1362, 1412]), Send, WaitMode.Wait],
    # auto-generated telemetry end



    ["Set bootslots for deep_sleep.", Print, WaitMode.Wait],
    [tc.SetBootSlots(200, 0b111000, 0b111), Send, WaitMode.Wait],

    # Wait for good uplink before power cycle
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]