tasks = [
    # Generated on 2019-02-17 17:46:41.516000, contains telemetry from sessions 490 to 491.
    # The session starts on 2019-02-17 19:42:01+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 120, 170]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970, 108, 158, 208, 258]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 908, 958, 132, 182, 232, 282, 332, 382]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932, 982, 102, 152, 202, 252, 302, 352, 402, 452]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [502, 552, 602, 652, 702, 752, 802, 852, 902, 952, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [614, 664, 714, 764, 814, 864, 914, 964, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [726, 776, 826, 876, 926, 976, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [838, 888, 938, 988]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # missings from 490 - low-res photos
    [tc.DownloadFile(40, '/p2_128_0', [0, 1, 3, 5, 8, 10, 14, 16, 17, 19, 20, 22, 26, 27, 29]), Send, WaitMode.Wait],
    [tc.DownloadFile(41, '/p5_128_0', [5]), Send, WaitMode.Wait],
    [tc.DownloadFile(42, '/p3_128_0', [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 18, 20, 23, 31]), Send, WaitMode.Wait],
    [tc.DownloadFile(43, '/telemetry.current', [25]), Send, WaitMode.Wait],

    # hi-res photos
    # p1_480_0 - 92
    [tc.DownloadFile(50, '/p1_480_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/p1_480_0', [i for i in range(23, 46, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/p1_480_0', [i for i in range(46, 69, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/p1_480_0', [i for i in range(69, 92, 1)]), Send, WaitMode.Wait],

    # p7_480_0 - 129
    [tc.DownloadFile(60, '/p7_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/p7_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/p7_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/p7_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/p7_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/p7_480_0', [i for i in range(104, 129, 1)]), Send, WaitMode.Wait],

    # p6_480_0 - 132
    [tc.DownloadFile(70, '/p6_480_0', [i for i in range(0, 26, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/p6_480_0', [i for i in range(26, 52, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/p6_480_0', [i for i in range(52, 78, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/p6_480_0', [i for i in range(78, 92, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/p6_480_0', [i for i in range(92, 104, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/p6_480_0', [i for i in range(104, 132, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]