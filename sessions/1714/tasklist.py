tasks = [
    # Generated on 2019-08-24 15:25:13.086000, contains telemetry from sessions 1712 to 1714.
    # The session starts on 2019-08-24 21:05:15+02:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(31, '/telemetry.current', [174, 224, 274, 324, 374, 424, 474, 524, 574, 624, 674, 724, 774, 824, 874, 924, 974, 1024, 1074, 1124]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1174, 1224, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [1099, 1149, 1199, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687, 737, 787, 837, 887, 937, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1037, 1087, 1137, 1187, 1237, 211, 261, 311, 361, 411, 461, 511, 561, 611, 661, 711, 761, 811, 861, 911]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [961, 1011, 1061, 1111, 1161, 1211, 181, 231, 281, 331, 381, 431, 481, 531, 581, 631, 681, 731, 781, 831]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [881, 931, 981, 1031, 1081, 1131, 1181, 1231, 193, 243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [793, 843, 893, 943, 993, 1043, 1093, 1143, 1193, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [755, 805, 855, 905, 955, 1005, 1055, 1105, 1155, 1205, 217, 267, 317, 367, 417, 467, 517, 567, 617, 667]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [717, 767, 817, 867, 917, 967, 1017, 1067, 1117, 1167, 1217, 1, 64, 82, 114, 132]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    [tc.DownloadFile(29, '/radfet_20', [9, 11]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    [tc.DownloadFile(53, '/x2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/x2_128_0', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(55, '/x1_480_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/x1_480_0', [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/x1_480_0', [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/x1_480_0', [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/x1_480_0', [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/x1_480_0', [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/x1_480_0', [114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/x1_480_0', [133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/x1_480_0', [152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(40, '/suns_ps_11', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_11', [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_11', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_11', [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_11', [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_11', [98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_11', [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_11', [136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_11', [155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_11', [174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_11', [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_11', [212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_11', [231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(64, '/p1_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p1_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/p2_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/p2_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/p3_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/p4_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p5_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p5_128_0', [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p6_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p7_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p8_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/p9_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/p9_128_0', [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(78, '/p10_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/p11_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/p11_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/p12_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/p13_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/p14_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/p15_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/p16_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/p16_128_0', [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/p17_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(88, '/p18_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/p18_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(90, '/p19_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(91, '/p20_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), Send, WaitMode.Wait],
    [tc.DownloadFile(92, '/p21_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(93, '/p22_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(94, '/p23_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(95, '/p23_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(96, '/p24_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]), Send, WaitMode.Wait],
    [tc.DownloadFile(97, '/p25_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Send, WaitMode.Wait],
    [tc.DownloadFile(98, '/p25_128_0', [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), Send, WaitMode.Wait],
    [tc.DownloadFile(99, '/p26_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/p26_128_0', [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), Send, WaitMode.Wait],
    
    [tc.DownloadFile(101, '/p27_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p28_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p29_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p30_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p31_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p32_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p33_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p34_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p35_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(110, '/p36_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p38_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/p39_128_0', [0, 1, 2, 3, 4]), Send, WaitMode.Wait],
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]