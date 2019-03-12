tasks = [
    # Generated on 2019-03-12 08:21:53.166320, contains telemetry from sessions 637 to 640.
    # The session starts on 2019-03-12 10:27:22+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1975, 2025, 2075, 2125, 2175, 2225, 2275, 2000, 2050, 2100, 2150, 2200, 2250, 1988, 2038, 2088, 2138, 2188, 2238, 2012]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [1045, 1095, 1145, 20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [870, 920, 970, 1020, 1070, 1120, 1170, 8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [658, 708, 758, 808, 858, 908, 958, 1008, 1058, 1108, 1158, 32, 82, 132, 182, 232, 282, 332, 382, 432]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2062, 2112, 2162, 2212, 2262, 1982, 2032, 2082, 2132, 2182, 2232, 1994, 2044, 2094, 2144, 2194, 2244, 2006, 2056, 2106]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 2, 52, 102, 152, 202]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 1002, 1052, 1102, 1152, 14]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864, 914, 964, 1014]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [1064, 1114, 1164, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.previous', [2156, 2206, 2256, 2018, 2068, 2118, 2168, 2218, 2268]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [876, 926, 976, 1026, 1076, 1126, 1176, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/telemetry.current', [688, 738, 788, 838, 888, 938, 988, 1038, 1088, 1138]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
