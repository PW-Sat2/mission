tasks = [
    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    [tc.ListFiles(2, '/'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # 11th RadFET Experiment
    [tc.PerformRadFETExperiment(10, 150, 110, 'radfet_12'), Send, WaitMode.Wait],

    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Low res photos download
	[tc.DownloadFile(103, '/p3_128_0', [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]), Send, WaitMode.Wait],

    [tc.DownloadFile(104, '/p4_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p4_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(106, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p5_128_0', [i for i in range(18, 29, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(108, '/p6_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p6_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(110, '/p7_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(111, '/p7_128_0', [i for i in range(18, 26, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(112, '/p8_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(113, '/p8_128_0', [i for i in range(18, 28, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(114, '/p9_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(115, '/p9_128_0', [i for i in range(18, 31, 1)]), Send, WaitMode.Wait],

    [tc.DownloadFile(116, '/p10_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(117, '/p10_128_0', [i for i in range(18, 36, 1)]), Send, WaitMode.Wait],


    # If good link, download daily telemetry
    [tc.DownloadFile(30, '/telemetry.current', [176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026, 201, 251]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [301, 351, 401, 451, 501, 551, 601, 651, 701, 751, 801, 851, 901, 951, 1001, 1051, 189, 239, 289, 339]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [389, 439, 489, 539, 589, 639, 689, 739, 789, 839, 889, 939, 989, 1039, 213, 263, 313, 363, 413, 463]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [513, 563, 613, 663, 713, 763, 813, 863, 913, 963, 1013, 1063, 183, 233, 283, 333, 383, 433, 483, 533]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [583, 633, 683, 733, 783, 833, 883, 933, 983, 1033, 195, 245, 295, 345, 395, 445, 495, 545, 595, 645]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [695, 745, 795, 845, 895, 945, 995, 1045, 207, 257, 307, 357, 407, 457, 507, 557, 607, 657, 707, 757]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [807, 857, 907, 957, 1007, 1057, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [919, 969, 1019, 1069]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', range(150, 176, 3)), Send, WaitMode.Wait],

    # Get beacons
    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]