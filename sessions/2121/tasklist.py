tasks = [
    # Generated on 2019-10-28 00:06:40.831000, contains telemetry from sessions 2118 to 2121.
    # The session starts on 2019-10-28 09:49:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(43, '/telemetry.current', [362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262, 1312]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/telemetry.current', [1362, 1412, 1462, 1512, 1562, 1612, 1662, 1712, 1762, 1812, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/telemetry.current', [887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 1337, 1387, 1437, 1487, 1537, 1587, 1637, 1687, 1737, 1787, 1837]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/telemetry.current', [375, 425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 1325]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/telemetry.current', [1375, 1425, 1475, 1525, 1575, 1625, 1675, 1725, 1775, 1825, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/telemetry.current', [899, 949, 999, 1049, 1099, 1149, 1199, 1249, 1299, 1349, 1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 369]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/telemetry.current', [419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 1319, 1369]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/telemetry.current', [1419, 1469, 1519, 1569, 1619, 1669, 1719, 1769, 1819, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831, 881]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 1331, 1381, 1431, 1481, 1531, 1581, 1631, 1681, 1731, 1781, 1831, 393]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 1243, 1293, 1343, 1393]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [1443, 1493, 1543, 1593, 1643, 1693, 1743, 1793, 1843, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855, 905]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/telemetry.current', [955, 1005, 1055, 1105, 1155, 1205, 1255, 1305, 1355, 1405, 1455, 1505, 1555, 1605, 1655, 1705, 1755, 1805]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(30, '/t02w_240_17', [40, 47]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/t02w_240_7', [12, 13, 14, 16, 17, 19, 23, 24, 25, 26, 33, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/t02w_240_7', [40, 41, 43, 46, 47, 48, 49, 50, 51, 53, 54, 55]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/t02w_240_9', [0, 2, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/t02w_240_9', [36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/t02w_240_27', [1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/t02w_240_27', [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/t02w_240_27', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/t02w_240_27', [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/t02w_240_28', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/t02w_240_28', [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/t02w_240_28', [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/t02w_240_28', [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]