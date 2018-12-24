tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate1200), 5], SendLoop, WaitMode.NoWait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # ReadMemory, weird telecommand
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],
    [tc.PingTelecommand(), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # Seventh RadFET Experiment
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.PerformRadFETExperiment(10, 150, 250, 'radfet_7'), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Telemetry between session 128 and 129
    [tc.DownloadFile(22, '/telemetry.current', [i for i in range(0, 100, 5)]), Send, WaitMode.Wait],

    [tc.DownloadFile(20, '/telemetry.previous', [i for i in range(1400, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(21, '/telemetry.previous', [i for i in range(1425, 2280, 50)]), Send, WaitMode.Wait],

    [tc.DownloadFile(23, '/telemetry.previous', [i for i in range(1412, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(24, '/telemetry.previous', [i for i in range(1437, 2280, 50)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(25, '/telemetry.previous', [i for i in range(1406, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(26, '/telemetry.previous', [i for i in range(1418, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(27, '/telemetry.previous', [i for i in range(1431, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(28, '/telemetry.previous', [i for i in range(1443, 2280, 50)]), Send, WaitMode.Wait],

    # Remove downloaded photos
    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(30, '/p1_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(31, '/p2_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(32, '/p3_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(33, '/p4_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(34, '/p5_128_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(35, '/p6_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(36, '/p7_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(37, '/p8_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(38, '/p9_128_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(39, '/p10_128_0'), Send, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],
    [tc.RemoveFile(40, '/p3_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(41, '/p7_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(42, '/p2_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(43, '/p1_480_0'), Send, WaitMode.NoWait],
    [tc.RemoveFile(44, '/radfet_6'), Send, WaitMode.NoWait],

    # More telemetry between session 128 and 129
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(50, '/telemetry.current', [i for i in range(1, 100, 5)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/telemetry.current', [i for i in range(2, 100, 5)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/telemetry.current', [i for i in range(3, 100, 5)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/telemetry.current', [i for i in range(4, 100, 5)]), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(54, '/telemetry.previous', [i for i in range(1403, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/telemetry.previous', [i for i in range(1409, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/telemetry.previous', [i for i in range(1415, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/telemetry.previous', [i for i in range(1421, 2280, 50)]), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.NoWait],
    [tc.DownloadFile(58, '/telemetry.previous', [i for i in range(1428, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/telemetry.previous', [i for i in range(1434, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/telemetry.previous', [i for i in range(1440, 2280, 50)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/telemetry.previous', [i for i in range(1446, 2280, 50)]), Send, WaitMode.Wait],

    # Missing telemetry between session 124 and 127
    [tc.DownloadFile(100, '/telemetry.previous', [0, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/telemetry.previous', [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/telemetry.previous', [67, 68, 69, 70, 80, 81, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 102, 103]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/telemetry.previous', [104, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]), Send, WaitMode.Wait], 
    [tc.DownloadFile(104, '/telemetry.previous', [125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 150, 151, 153, 154, 155]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/telemetry.previous', [156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 171, 172, 173, 174, 176, 177]), Send, WaitMode.Wait], 
    [tc.DownloadFile(106, '/telemetry.previous', [178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/telemetry.previous', [198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 221, 223, 224, 225, 226, 227, 228, 229]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/telemetry.previous', [230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 241, 242, 243, 244, 246, 247, 248, 249, 250, 251]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/telemetry.previous', [252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271]), Send, WaitMode.Wait], 
    [tc.DownloadFile(110, '/telemetry.previous', [272, 273, 274, 275, 276, 277, 278, 279, 291, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303]), Send, WaitMode.Wait], 
    [tc.DownloadFile(111, '/telemetry.previous', [304, 305, 306, 307, 308, 309, 311, 312, 313, 314, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325]), Send, WaitMode.Wait],
    [tc.DownloadFile(112, '/telemetry.previous', [326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/telemetry.previous', [346, 347, 348, 349, 360, 361, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376]), Send, WaitMode.Wait],
    [tc.DownloadFile(114, '/telemetry.previous', [377, 378, 379, 381, 382, 383, 384, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/telemetry.previous', [399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418]), Send, WaitMode.Wait],
    [tc.DownloadFile(116, '/telemetry.previous', [419, 431, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 451]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/telemetry.previous', [452, 453, 454, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472]), Send, WaitMode.Wait],
    [tc.DownloadFile(118, '/telemetry.previous', [473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 501, 503, 504]), Send, WaitMode.Wait],
    [tc.DownloadFile(119, '/telemetry.previous', [505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 521, 522, 523, 524, 526]), Send, WaitMode.Wait],
    [tc.DownloadFile(120, '/telemetry.previous', [527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546]), Send, WaitMode.Wait],
    [tc.DownloadFile(121, '/telemetry.previous', [547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 571, 573, 574, 575, 576, 577, 578]), Send, WaitMode.Wait],
    [tc.DownloadFile(122, '/telemetry.previous', [579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 591, 592, 593, 594, 596, 597, 598, 599, 600]), Send, WaitMode.Wait],
    [tc.DownloadFile(123, '/telemetry.previous', [601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620]), Send, WaitMode.Wait],
    [tc.DownloadFile(124, '/telemetry.previous', [621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 641, 643, 644, 645, 646, 647, 648, 649, 650, 651]), Send, WaitMode.Wait],
    [tc.DownloadFile(125, '/telemetry.previous', [652, 653, 654, 655, 656, 657, 658, 659, 661, 662, 663, 664, 666, 667, 668, 669, 670, 671, 672, 673]), Send, WaitMode.Wait],
    [tc.DownloadFile(126, '/telemetry.previous', [674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693]), Send, WaitMode.Wait],
    [tc.DownloadFile(127, '/telemetry.previous', [694, 695, 696, 697, 698, 699, 700, 711, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724]), Send, WaitMode.Wait],
    [tc.DownloadFile(128, '/telemetry.previous', [725, 726, 727, 728, 729, 731, 732, 733, 734, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746]), Send, WaitMode.Wait],
    [tc.DownloadFile(129, '/telemetry.previous', [747, 748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766]), Send, WaitMode.Wait],
    [tc.DownloadFile(130, '/telemetry.previous', [767, 768, 769, 781, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798]), Send, WaitMode.Wait],
    [tc.DownloadFile(131, '/telemetry.previous', [799, 801, 802, 803, 804, 806, 807, 808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820]), Send, WaitMode.Wait],
    [tc.DownloadFile(132, '/telemetry.previous', [821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840]), Send, WaitMode.Wait],
    [tc.DownloadFile(133, '/telemetry.previous', [851, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 871, 872]), Send, WaitMode.Wait],
    [tc.DownloadFile(134, '/telemetry.previous', [873, 874, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893]), Send, WaitMode.Wait],
    [tc.DownloadFile(135, '/telemetry.previous', [894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 921, 923, 924, 925]), Send, WaitMode.Wait],
    [tc.DownloadFile(136, '/telemetry.previous', [926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 941, 942, 943, 944, 946, 947]), Send, WaitMode.Wait],
    [tc.DownloadFile(137, '/telemetry.previous', [948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967]), Send, WaitMode.Wait],
    [tc.DownloadFile(138, '/telemetry.previous', [968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 991, 993, 994, 995, 996, 997, 998, 999]), Send, WaitMode.Wait],
    [tc.DownloadFile(139, '/telemetry.previous', [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1011, 1012, 1013, 1014, 1016, 1017]), Send, WaitMode.Wait],
    [tc.DownloadFile(140, '/telemetry.previous', [1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033]), Send, WaitMode.Wait],
    [tc.DownloadFile(141, '/telemetry.previous', [1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049]), Send, WaitMode.Wait],
    [tc.DownloadFile(142, '/telemetry.previous', [1061, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077]), Send, WaitMode.Wait],
    [tc.DownloadFile(143, '/telemetry.previous', [1078, 1079, 1081, 1082, 1083, 1084, 1086, 1087, 1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095]), Send, WaitMode.Wait],
    [tc.DownloadFile(144, '/telemetry.previous', [1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109, 1110, 1111]), Send, WaitMode.Wait],
    [tc.DownloadFile(145, '/telemetry.previous', [1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1131, 1133, 1134, 1135, 1136, 1137, 1138]), Send, WaitMode.Wait],
    [tc.DownloadFile(146, '/telemetry.previous', [1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147, 1148, 1149, 1151, 1152, 1153, 1154, 1156]), Send, WaitMode.Wait],
    [tc.DownloadFile(147, '/telemetry.previous', [1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172]), Send, WaitMode.Wait],
    [tc.DownloadFile(148, '/telemetry.previous', [1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188]), Send, WaitMode.Wait],
    [tc.DownloadFile(149, '/telemetry.previous', [1189, 1190, 1201, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215]), Send, WaitMode.Wait],
    [tc.DownloadFile(150, '/telemetry.previous', [1216, 1217, 1218, 1219, 1221, 1222, 1223, 1224, 1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233]), Send, WaitMode.Wait],
    [tc.DownloadFile(151, '/telemetry.previous', [1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249]), Send, WaitMode.Wait],
    [tc.DownloadFile(152, '/telemetry.previous', [1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1271, 1273, 1274, 1275, 1276, 1277]), Send, WaitMode.Wait],
    [tc.DownloadFile(153, '/telemetry.previous', [1278, 1279, 1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1291, 1292, 1293, 1294]), Send, WaitMode.Wait],
    [tc.DownloadFile(154, '/telemetry.previous', [1296, 1297, 1298, 1299, 1300, 1301, 1302, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310, 1311]), Send, WaitMode.Wait],
    [tc.DownloadFile(155, '/telemetry.previous', [1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1328, 1329, 1341]), Send, WaitMode.Wait],


    [tc.SendBeacon(), Send, WaitMode.Wait],
]