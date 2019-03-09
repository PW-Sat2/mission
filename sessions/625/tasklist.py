tasks = [
    # Generated on 2019-03-09 12:14:36.366000, contains telemetry from sessions 621 to 625.
    # The session starts on 2019-03-09 21:08:53+01:00.

    [[tc.SetBitrate(1, BaudRate.BaudRate9600), 5], SendLoop, WaitMode.NoWait],

    [[tc.SendBeacon(), 10], SendLoop, WaitMode.NoWait],

    # ReadMemory, weird telecommands
    [tc.ReadMemory(2, 0x8801b620, 248), Send, WaitMode.Wait], # scrubbing

    # Wait until good communication
    [tc.SendBeacon(), Send, WaitMode.Wait],

    # Power cycle EPS B
    [tc.PowerCycleTelecommand(3), Send, WaitMode.Wait],

    [tc.PingTelecommand(), Send, WaitMode.Wait],

    # Set 9600
    [tc.SetBitrate(4, BaudRate.BaudRate9600), Send, WaitMode.Wait],
    [tc.SendBeacon(), Send, WaitMode.Wait],

    [tc.ListFiles(5, '/'), Send, WaitMode.Wait],

    # auto-generated telemetry start
    [tc.DownloadFile(30, '/telemetry.current', [69, 119, 169, 219, 269, 319, 369, 419, 469, 519, 569, 619, 669, 719, 769, 819, 869, 919, 969, 1019]), Send, WaitMode.Wait],
    [tc.DownloadFile(31, '/telemetry.current', [1069, 1119, 1169, 1219, 1269, 94, 144, 194, 244, 294, 344, 394, 444, 494, 544, 594, 644, 694, 744, 794]), Send, WaitMode.Wait],
    [tc.DownloadFile(32, '/telemetry.current', [844, 894, 944, 994, 1044, 1094, 1144, 1194, 1244, 1294, 82, 132, 182, 232, 282, 332, 382, 432, 482, 532]), Send, WaitMode.Wait],
    [tc.DownloadFile(33, '/telemetry.current', [582, 632, 682, 732, 782, 832, 882, 932, 982, 1032, 1082, 1132, 1182, 1232, 1282, 106, 156, 206, 256, 306]), Send, WaitMode.Wait],
    [tc.DownloadFile(34, '/telemetry.current', [356, 406, 456, 506, 556, 606, 656, 706, 756, 806, 856, 906, 956, 1006, 1056, 1106, 1156, 1206, 1256, 1306]), Send, WaitMode.Wait],
    [tc.DownloadFile(35, '/telemetry.current', [76, 126, 176, 226, 276, 326, 376, 426, 476, 526, 576, 626, 676, 726, 776, 826, 876, 926, 976, 1026]), Send, WaitMode.Wait],
    [tc.DownloadFile(36, '/telemetry.current', [1076, 1126, 1176, 1226, 1276, 88, 138, 188, 238, 288, 338, 388, 438, 488, 538, 588, 638, 688, 738, 788]), Send, WaitMode.Wait],
    [tc.DownloadFile(37, '/telemetry.current', [838, 888, 938, 988, 1038, 1088, 1138, 1188, 1238, 1288, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550]), Send, WaitMode.Wait],
    [tc.DownloadFile(38, '/telemetry.current', [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 112, 162, 212, 262, 312]), Send, WaitMode.Wait],
    [tc.DownloadFile(39, '/telemetry.current', [362, 412, 462, 512, 562, 612, 662, 712, 762, 812, 862, 912, 962, 1012, 1062, 1112, 1162, 1212, 1262]), Send, WaitMode.Wait],
    # auto-generated telemetry end

    # Low res photos download
    [tc.DownloadFile(99, '/p1_128_0', [i for i in range(0, 20, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(100, '/p1_128_0', [i for i in range(20, 37, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(101, '/p2_128_0', [i for i in range(0, 29, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(102, '/p3_128_0', [i for i in range(0, 28, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(103, '/p4_128_0', [i for i in range(0, 14, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(104, '/p5_128_0', [i for i in range(0, 18, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(105, '/p6_128_0', [i for i in range(0, 16, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(106, '/p7_128_0', [i for i in range(0, 30, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(107, '/p8_128_0', [i for i in range(0, 15, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(108, '/p9_128_0', [i for i in range(0, 23, 1)]), Send, WaitMode.Wait],
    [tc.DownloadFile(109, '/p10_128_0', [i for i in range(0, 14, 1)]), Send, WaitMode.Wait],

    [[tc.SendBeacon(), 20], SendLoop, WaitMode.NoWait],
]