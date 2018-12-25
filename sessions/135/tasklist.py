tasks = [
    # ============================================================================
    # SESSION 135
    # ============================================================================

    ["SESSION 135", Print, WaitMode.NoWait],

    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # ReadMemory, weird telecommand
    ["ReadMemory, weird telecommand", Print, WaitMode.NoWait],
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    ["List files - 7 items expected", Print, WaitMode.NoWait],
    [tc.ListFiles(3, '/'), Send, WaitMode.Wait],

    # Wait until good uplink
    ["Beacons - Wait until good uplink - next one is POWER CYCLE", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # EPS A - Power cycle - send three times (no answer expected!)
    ["EPS A - Power cycle - send three times (no answer expected!)", Print, WaitMode.NoWait],
    [tc.RawI2C(4, 0, 0x35, 1, [0xE0]), Send, WaitMode.Wait],

    # Ping - start pinging about 30 s after reboot
    ["Ping - start pinging about 30 s after reboot", Print, WaitMode.NoWait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Wait for non-zero beacon
    ["Request till non-zero beacon decoded", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],


    # Set 9600
    ["Set 9600", Print, WaitMode.NoWait],
    [tc.SetBitrate(10, BaudRate.BaudRate9600), Send, WaitMode.Wait],

    # Get beacon at 9600
    ["Get beacon at 9600", Print, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry.current between session 134 and 135
    ["Telemetry current between sessions  134 and 135", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(20, '/telemetry.current', [i for i in range(0, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.current', [i for i in range(14, 380, 25)]), Send, WaitMode.Wait],

    # Telemetry previous from 1760 to 2280 chunks
    ["Telemetry previous from 1760 to 2280 chunks", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(30, '/telemetry.previous', [i for i in range(1760, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.previous', [i for i in range(1764, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.previous', [i for i in range(1769, 2280, 25)]), Send, WaitMode.Wait],


    # More telemetry.current between session 134 and 135
    ["More telemetry current between sessions  134 and 135", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(40, '/telemetry.current', [i for i in range(4, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [i for i in range(9, 380, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [i for i in range(19, 380, 25)]), Send, WaitMode.Wait],

    # More telemetry previous from 1760 to 2280 chunks
    ["More telemetry previous from 1760 to 2280 chunks", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.previous', [i for i in range(1774, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.previous', [i for i in range(1779, 2280, 25)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.previous', [i for i in range(1784, 2280, 25)]), Send, WaitMode.Wait],


    # Remove radfet file
    ["Remove file", Print, WaitMode.Wait],
    [tc.RemoveFile(60, '/radfet_7'), Send, WaitMode.Wait],
    [tc.ListFiles(61, '/'), Send, WaitMode.Wait],


    # Previously not downloaded telemetry.previous
    ["Previously not downloaded telemetry.previous", Print, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(100, '/telemetry.previous', [317, 332, 340, 342, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [377, 385, 392, 404, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 437, 452]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [462, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 497, 512, 521]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [522, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 557, 572, 582]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/telemetry.previous', [584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 617, 632, 644, 645]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 677, 692, 701, 704, 706, 707]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/telemetry.previous', [708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 737, 752, 762, 764, 765, 766, 767]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 797, 812, 824, 825, 826, 827, 828, 829]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 857, 872, 882, 884, 886, 888, 889, 890, 891, 892]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [893, 894, 895, 896, 897, 898, 899, 917, 932, 944, 946, 948, 949, 950, 951, 952, 953, 954, 955, 956]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/telemetry.previous', [957, 958, 959, 960, 977, 992, 1004, 1005, 1006, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/telemetry.previous', [1019, 1032, 1037, 1052, 1064, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1092]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [1097, 1112, 1124, 1126, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1152, 1157, 1172]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.previous', [1180, 1184, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1212, 1217, 1225, 1232]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [1236, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1272, 1277, 1292]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/telemetry.previous', [1300, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1337, 1352, 1362]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/telemetry.previous', [1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375, 1376, 1377, 1378, 1379, 1397, 1412, 1422, 1424]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.previous', [1425, 1426, 1427, 1428, 1429, 1430, 1431, 1433, 1434, 1435, 1437, 1438, 1439, 1440, 1457, 1472, 1484, 1485, 1486, 1487]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.previous', [1488, 1489, 1490, 1491, 1492, 1493, 1494, 1495, 1496, 1497, 1498, 1499, 1517, 1540, 1542, 1544, 1545, 1546, 1547, 1548]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/telemetry.previous', [1550, 1551, 1553, 1555, 1556, 1557, 1558, 1559, 1577, 1592]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
]