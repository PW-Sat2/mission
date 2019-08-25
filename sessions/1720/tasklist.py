tasks = [
    # Generated on 2019-08-25 13:49:25.071000, contains telemetry from sessions 1719 to 1720.
    # The session starts on 2019-08-25 21:05:10+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(57, '/telemetry.current', [712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312, 1362, 1412, 1462, 1512, 1562, 737, 787]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/telemetry.current', [837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 725, 775, 825, 875]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.current', [925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325, 1375, 1425, 1475, 1525, 1575, 749, 799, 849, 899, 949, 999]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.current', [1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 719, 769, 819, 869, 919, 969, 1019, 1069]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.current', [1119, 1169, 1219, 1269, 1319, 1369, 1419, 1469, 1519, 1569, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/telemetry.current', [1231, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/telemetry.current', [1343, 1393, 1443, 1493, 1543, 1593, 755, 805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/telemetry.current', [1455, 1505, 1555, 551, 575, 701]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(41, '/p12_128_0', [11]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/p22_128_0', [1]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/p19_128_0', [1, 5]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/p15_128_0', [3]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/p11_128_0', [0, 2, 8, 16, 18, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/p21_128_0', [0, 2, 3, 7, 12, 13, 14]), Send, WaitMode.Wait],

    [tc.DownloadFile(35, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p18_128_0', [0, 1, 2, 3, 7, 10, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    # missing from previous session pause

    # auto-generated file download start
    [tc.DownloadFile(65, '/t12n_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/t12w_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/t12w_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/t12w_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/t12w_480_0', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/t12w_480_0', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/t12w_480_0', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/t12w_480_0', [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/t12w_480_0', [99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/t12w_480_0', [118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/t12w_480_0', [137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155]), Send, WaitMode.Wait],
    # auto-generated file download end

    # missing from previous session resume
    [tc.DownloadFile(36, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(30, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # missing from previous session end

    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]