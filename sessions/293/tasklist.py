tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [2106, 2156, 2206, 2256, 2131, 2181, 2231, 2119, 2169, 2219, 2269, 2143, 2193, 2243, 2113, 2163, 2213, 2263, 2125, 2175]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1026, 1076, 1126, 1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [851, 901, 951, 1001, 1051, 1101, 39, 89, 139, 189, 239, 289, 339, 389, 439, 489, 539, 589, 639, 689]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [739, 789, 839, 889, 939, 989, 1039, 1089, 1139, 13, 63, 113, 163, 213, 263, 313, 363, 413, 463, 513]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 1113, 33, 83, 133, 183, 233, 283, 333, 383]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [433, 483, 533, 583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 1083, 1133, 45, 95, 145, 195, 245]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.previous', [2225, 2275, 2137, 2187, 2237, 2149, 2199, 2249]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045, 1095, 7, 57, 107]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [157, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757, 807, 857, 907, 957, 1007, 1057, 1107]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [19, 69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [1019, 1069, 1119]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]