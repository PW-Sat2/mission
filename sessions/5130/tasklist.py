tasks = [
    # Generated on 2021-02-09 21:18:48.914000, contains telemetry from sessions 5128 to 5130.
    # The session starts on 2021-02-09 22:32:34+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(32, '/telemetry.current', [45, 95, 145, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [20, 70, 120, 170, 220, 270, 320, 370, 420, 470, 520, 570, 620, 670, 720, 770, 820, 870, 920, 970]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [8, 58, 108, 158, 208, 258, 308, 358, 408, 458, 508, 558, 608, 658, 708, 758, 808, 858, 908, 958]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [1008, 32, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532, 582, 632, 682, 732, 782, 832, 882, 932]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [982, 2, 52, 102, 152, 202, 252, 302, 352, 402, 452, 502, 552, 602, 652, 702, 752, 802, 852, 902]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [952, 1002, 14, 64, 114, 164, 214, 264, 314, 364, 414, 464, 514, 564, 614, 664, 714, 764, 814, 864]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [914, 964, 1014, 26, 76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [876, 926, 976, 38, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788, 838]), Send, WaitMode.Wait],
    [tc.DownloadFile(40, '/telemetry.current', [888, 938, 988]), Send, WaitMode.Wait],
    # auto-generated telemetry end


    [tc.DownloadFile(50, '/n01w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(51, '/n01w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(52, '/n01w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(53, '/n01w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(54, '/n01w_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(55, '/n01w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(56, '/n01w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(57, '/n01w_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(60, '/n01n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(61, '/n01n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(62, '/n01n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(63, '/n01n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(64, '/n01n_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(65, '/n01n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(66, '/n01n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(67, '/n01n_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(70, '/n02w_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(71, '/n02w_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(72, '/n02w_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(73, '/n02w_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(74, '/n02w_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(75, '/n02w_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(76, '/n02w_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(77, '/n02w_0', range(140, 160)), Send, WaitMode.Wait],

    [tc.DownloadFile(80, '/n02n_0', range(0, 20)), Send, WaitMode.Wait],
    [tc.DownloadFile(81, '/n02n_0', range(20, 40)), Send, WaitMode.Wait],
    [tc.DownloadFile(82, '/n02n_0', range(40, 60)), Send, WaitMode.Wait],
    [tc.DownloadFile(83, '/n02n_0', range(60, 80)), Send, WaitMode.Wait],
    [tc.DownloadFile(84, '/n02n_0', range(80, 100)), Send, WaitMode.Wait],
    [tc.DownloadFile(85, '/n02n_0', range(100, 120)), Send, WaitMode.Wait],
    [tc.DownloadFile(86, '/n02n_0', range(120, 140)), Send, WaitMode.Wait],
    [tc.DownloadFile(87, '/n02n_0', range(140, 160)), Send, WaitMode.Wait],

    # missing from previous session start
    
    # missing from previous session end


    # auto-generated file download start
    
    # auto-generated file download end


    # auto-generated file remove start
    
    # auto-generated file remove end


    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]