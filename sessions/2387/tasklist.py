tasks = [
    # Generated on 2019-12-07 10:00:48.378374, contains telemetry from sessions 2386 to 2387.
    # The session starts on 2019-12-07 11:08:33+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(88, '/telemetry.current', [1450, 1500, 1550, 1600, 1650, 1475, 1525, 1575, 1625, 1463, 1513, 1563, 1613, 1663, 1487, 1537, 1587, 1637, 1457, 1507]), Send, WaitMode.Wait],
    [tc.DownloadFile(89, '/telemetry.current', [1557, 1607, 1657, 1469, 1519, 1569, 1619, 1669, 1481, 1531, 1581, 1631, 1493, 1543, 1593, 1643, 1443]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Long Movie Over Europe, don't have to wait
    [tc.TakePhotoTelecommand(100, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(minutes=2), 't01w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(101, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(seconds=0), 't02w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(102, CameraLocation.Wing, PhotoResolution.p240, 29, datetime.timedelta(seconds=0), 't03w_240'), Send, WaitMode.Wait],
    [tc.TakePhotoTelecommand(103, CameraLocation.Wing, PhotoResolution.p240, 7, datetime.timedelta(seconds=0), 't04w_240'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # missing from previous session start
    [tc.DownloadFile(31, '/suns_ps_16', [47, 48, 59, 60, 62, 63, 64, 65, 66, 102, 114, 119, 120, 121, 122, 123, 124, 125, 126, 127]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/suns_ps_16', [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/suns_ps_16', [148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/suns_ps_16', [168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/suns_ps_16', [188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/suns_ps_16', [208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/suns_ps_16', [228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/suns_ps_16', [248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/suns_ps_16', [268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/suns_ps_16', [288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/suns_ps_16', [308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/suns_ps_16', [328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/suns_ps_16', [348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367]), Send, WaitMode.Wait],
    [tc.DownloadFile(44, '/suns_ps_16', [368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387]), Send, WaitMode.Wait],
    [tc.DownloadFile(45, '/suns_ps_16', [388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407]), Send, WaitMode.Wait],
    [tc.DownloadFile(46, '/suns_ps_16', [408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427]), Send, WaitMode.Wait],
    [tc.DownloadFile(47, '/suns_ps_16', [428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447]), Send, WaitMode.Wait],
    [tc.DownloadFile(48, '/suns_ps_16', [448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467]), Send, WaitMode.Wait],
    [tc.DownloadFile(49, '/suns_ps_16', [468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487]), Send, WaitMode.Wait],
    [tc.DownloadFile(50, '/suns_ps_16', [488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/suns_ps_16', [508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/suns_ps_16', [528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/suns_ps_16', [548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567]), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/suns_ps_16', [568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587]), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/suns_ps_16', [588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607]), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/suns_ps_16', [608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627]), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/suns_ps_16', [628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647]), Send, WaitMode.Wait],
    [tc.DownloadFile(58, '/suns_ps_16', [648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667]), Send, WaitMode.Wait],
    [tc.DownloadFile(59, '/suns_ps_16', [668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 687]), Send, WaitMode.Wait],
    [tc.DownloadFile(60, '/suns_ps_16', [688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 706, 707]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/suns_ps_16', [708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726, 727]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/suns_ps_16', [728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/suns_ps_16', [748, 749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/suns_ps_16', [768, 769, 770, 771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/suns_ps_16', [788, 789, 790, 791, 792, 793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807]), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/suns_ps_16', [808, 809, 810, 811, 812, 813, 814, 815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827]), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/suns_ps_16', [828, 829, 830, 831, 832, 833, 834, 835, 836, 837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847]), Send, WaitMode.Wait],
    [tc.DownloadFile(68, '/suns_ps_16', [848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 866, 867]), Send, WaitMode.Wait],
    [tc.DownloadFile(69, '/suns_ps_16', [868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880, 881, 882, 883, 884, 885, 886, 887]), Send, WaitMode.Wait],
    [tc.DownloadFile(70, '/suns_ps_16', [888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/suns_ps_16', [908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924, 925, 926, 927]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/suns_ps_16', [928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946, 947]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/suns_ps_16', [948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/suns_ps_16', [968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/suns_ps_16', [988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007]), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/suns_ps_16', [1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027]), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/suns_ps_16', [1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047]), Send, WaitMode.Wait],
    [tc.DownloadFile(78, '/suns_ps_16', [1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067]), Send, WaitMode.Wait],
    [tc.DownloadFile(79, '/suns_ps_16', [1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087]), Send, WaitMode.Wait],
    [tc.DownloadFile(80, '/suns_ps_16', [1088, 1089, 1090, 1091, 1092, 1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107]), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/suns_ps_16', [1108, 1109, 1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126, 1127]), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/suns_ps_16', [1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143, 1144, 1145, 1146, 1147]), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/suns_ps_16', [1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1167]), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/suns_ps_16', [1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187]), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/suns_ps_16', [1188, 1189, 1190, 1191, 1192, 1193, 1194, 1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206]), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/suns_ps_16', [1207, 1208, 1209, 1210, 1211, 1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225]), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/suns_ps_16', [1226, 1227, 1228, 1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244]), Send, WaitMode.Wait],
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]