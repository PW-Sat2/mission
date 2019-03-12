tasks = [
    # Generated on 2019-03-12 07:47:52.081617, contains telemetry from sessions 637 to 639.
    # The session starts on 2019-03-12 08:52:44+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.previous', [1975, 2025, 2075, 2125, 2175, 2225, 2275, 2000, 2050, 2100, 2150, 2200, 2250, 1988, 2038, 2088, 2138, 2188, 2238, 2012]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 908, 958]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [1008, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.previous', [2062, 2112, 2162, 2212, 2262, 1982, 2032, 2082, 2132, 2182, 2232, 1994, 2044, 2094, 2144, 2194, 2244, 2006, 2056, 2106]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [982, 2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [952, 1002, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [914, 964, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.previous', [2156, 2206, 2256, 2018, 2068, 2118, 2168, 2218, 2268]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [926, 976, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838, 888]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/telemetry.current', [938, 988]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]
