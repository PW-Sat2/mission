tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2092, 2142, 2192, 2242, 2117, 2167, 2217, 2267, 2105, 2155, 2205, 2255, 2129, 2179, 2229, 2279, 2099, 2149, 2199, 2249]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [12, 62, 112, 162, 212, 262, 312, 362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1012, 1062, 1112, 1162, 1212, 1262, 37, 87, 137, 187, 237, 287, 337, 387, 437, 487, 537, 587, 637, 687]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [737, 787, 837, 887, 937, 987, 1037, 1087, 1137, 1187, 1237, 1287, 25, 75, 125, 175, 225, 275, 325, 375]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [425, 475, 525, 575, 625, 675, 725, 775, 825, 875, 925, 975, 1025, 1075, 1125, 1175, 1225, 1275, 49, 99]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [149, 199, 249, 299, 349, 399, 449, 499, 549, 599, 649, 699, 749, 799, 849, 899, 949, 999, 1049, 1099]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1149, 1199, 1249, 1299, 19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [819, 869, 919, 969, 1019, 1069, 1119, 1169, 1219, 1269, 31, 81, 131, 181, 231, 281, 331, 381, 431, 481]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.previous', [2111, 2161, 2211, 2261, 2123, 2173, 2223, 2273, 2135, 2185, 2235]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [531, 581, 631, 681, 731, 781, 831, 881, 931, 981, 1031, 1081, 1131, 1181, 1231, 1281, 43, 93, 143, 193]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [243, 293, 343, 393, 443, 493, 543, 593, 643, 693, 743, 793, 843, 893, 943, 993, 1043, 1093, 1143, 1193]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1243, 1293, 5, 55, 105, 155, 205, 255, 305, 355, 405, 455, 505, 555, 605, 655, 705, 755, 805, 855]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [905, 955, 1005, 1055, 1105, 1155, 1205, 1255]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]