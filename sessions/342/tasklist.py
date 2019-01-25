tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2170, 2220, 2270, 2195, 2245, 2183, 2233, 2207, 2257, 2177, 2227, 2277, 2189, 2239, 2201, 2251, 2213, 2263]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1040, 1090, 1140, 1190, 1240, 1290, 1340, 15, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [665, 715, 765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 1315, 1365, 3, 53, 103, 153, 203]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [253, 303, 353, 403, 453, 503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1253, 1303, 1353, 27, 77, 127, 177, 227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [877, 927, 977, 1027, 1077, 1127, 1177, 1227, 1277, 1327, 1377, 47, 97, 147, 197, 247, 297, 347, 397, 447]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [497, 547, 597, 647, 697, 747, 797, 847, 897, 947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 1347, 9, 59]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609, 659, 709, 759, 809, 859, 909, 959, 1009, 1059]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1109, 1159, 1209, 1259, 1309, 1359, 21, 71, 121, 171, 221, 271, 321, 371, 421, 471, 521, 571, 621, 671]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 1321, 1371, 33, 83, 133, 183, 233, 283]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 1183, 1233, 1283]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [1333]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]