tasks = [
    # Generated on 2021-02-06 23:53:35.365985, contains telemetry from sessions 5115 to 5116.
    # The session starts on 2021-02-07 10:43:41+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [40, 90, 140, 190, 240, 290, 340, 390, 440, 490, 540, 590, 640, 690, 740, 790, 840, 890, 940, 990]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1040, 1090, 1140, 1190, 1240, 1290, 65, 115, 165, 215, 265, 315, 365, 415, 465, 515, 565, 615, 665, 715]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [765, 815, 865, 915, 965, 1015, 1065, 1115, 1165, 1215, 1265, 53, 103, 153, 203, 253, 303, 353, 403, 453]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [503, 553, 603, 653, 703, 753, 803, 853, 903, 953, 1003, 1053, 1103, 1153, 1203, 1253, 1303, 77, 127, 177]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [227, 277, 327, 377, 427, 477, 527, 577, 627, 677, 727, 777, 827, 877, 927, 977, 1027, 1077, 1127, 1177]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1227, 1277, 47, 97, 147, 197, 247, 297, 347, 397, 447, 497, 547, 597, 647, 697, 747, 797, 847, 897]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [947, 997, 1047, 1097, 1147, 1197, 1247, 1297, 59, 109, 159, 209, 259, 309, 359, 409, 459, 509, 559, 609]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [659, 709, 759, 809, 859, 909, 959, 1009, 1059, 1109, 1159, 1209, 1259, 71, 121, 171, 221, 271, 321, 371]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [421, 471, 521, 571, 621, 671, 721, 771, 821, 871, 921, 971, 1021, 1071, 1121, 1171, 1221, 1271, 83, 133]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [183, 233, 283, 333, 383, 433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [1183, 1233, 1283]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]